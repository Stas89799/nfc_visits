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
    middle_name = db.Column(db.String(150), nullable=True)
    birth_date = db.Column(db.String(150), nullable=True)
    phone = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=True)
    instagram = db.Column(db.String(150), nullable=True)
    telegram = db.Column(db.String(150), nullable=True)
    facebook = db.Column(db.String(150), nullable=True)
    whatsapp = db.Column(db.String(150), nullable=True)
    address = db.Column(db.String(150), nullable=True)
    photo = db.Column(db.String(150), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('cards', lazy=True))