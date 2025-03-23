from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, CardForm
from main import User, Card  # Обновите импорт, чтобы использовать main
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('create_card'))
    return render_template('register.html', form=form)

@app.route('/create_card', methods=['GET', 'POST'])
def create_card():
    form = CardForm()
    if form.validate_on_submit():
        card = Card(first_name=form.first_name.data, last_name=form.last_name.data, phone=form.phone.data)
        db.session.add(card)
        db.session.commit()
        flash('Card created successfully!', 'success')
        return redirect(url_for('view_card', card_id=card.id))
    return render_template('card.html', form=form)

@app.route('/card/<int:card_id>')
def view_card(card_id):
    card = Card.query.get_or_404(card_id)
    return render_template('view_card.html', card=card)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)