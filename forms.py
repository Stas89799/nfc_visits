from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, DateField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class CardForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    birth_date = DateField('Birth Date', format='%Y-%m-%d')
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email')
    instagram = StringField('Instagram')
    telegram = StringField('Telegram')
    facebook = StringField('Facebook')
    whatsapp = StringField('Whatsapp')
    address = StringField('Address')
    photo = FileField('Photo')
    submit = SubmitField('Save')