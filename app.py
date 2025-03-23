from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm, CardForm
from main import User, Card, db  # Обновите импорт, чтобы использовать main и db
import os
from werkzeug.utils import secure_filename
from config import Config  # Импортируем Config

app = Flask(__name__)
app.config.from_object(Config)  # Загружаем конфигурацию
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Проверка на уникальность имени пользователя
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user is None:
            user = User(username=form.username.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('create_card'))
        else:
            flash('Username already exists. Please choose a different username.', 'danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
        if user:
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/create_card', methods=['GET', 'POST'])
def create_card():
    form = CardForm()
    if form.validate_on_submit():
        # Сохранение фото
        file = form.photo.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None

        card = Card(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            middle_name=form.middle_name.data,
            birth_date=form.birth_date.data.strftime('%Y-%m-%d') if form.birth_date.data else None,
            phone=form.phone.data,
            email=form.email.data,
            instagram=form.instagram.data,
            telegram=form.telegram.data,
            facebook=form.facebook.data,
            whatsapp=form.whatsapp.data,
            address=form.address.data,
            photo=filename,
            user_id=session['user_id']
        )
        db.session.add(card)
        db.session.commit()
        flash('Card created successfully!', 'success')
        return redirect(url_for('view_card', card_id=card.id))
    return render_template('card.html', form=form)

@app.route('/card/<int:card_id>')
def view_card(card_id):
    card = Card.query.get_or_404(card_id)
    return render_template('view_card.html', card=card)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    user_id = session.get('user_id')
    if not user_id:
        flash('Please log in to edit your profile.', 'warning')
        return redirect(url_for('login'))

    card = Card.query.filter_by(user_id=user_id).first()
    if not card:
        flash('No profile found for this user.', 'warning')
        return redirect(url_for('create_card'))

    form = CardForm(obj=card)
    if form.validate_on_submit():
        file = form.photo.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            card.photo = filename

        card.first_name = form.first_name.data
        card.last_name = form.last_name.data
        card.middle_name = form.middle_name.data
        card.birth_date = form.birth_date.data.strftime('%Y-%m-%d') if form.birth_date.data else None
        card.phone = form.phone.data
        card.email = form.email.data
        card.instagram = form.instagram.data
        card.telegram = form.telegram.data
        card.facebook = form.facebook.data
        card.whatsapp = form.whatsapp.data
        card.address = form.address.data

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('view_card', card_id=card.id))
    return render_template('edit_profile.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)