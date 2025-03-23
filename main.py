from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    middle_name = db.Column(db.String(150))  # Убедитесь, что поле middle_name добавлено
    birth_date = db.Column(db.String(150))
    phone = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150))
    instagram = db.Column(db.String(150))
    telegram = db.Column(db.String(150))
    facebook = db.Column(db.String(150))
    whatsapp = db.Column(db.String(150))
    address = db.Column(db.String(150))
    photo = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)