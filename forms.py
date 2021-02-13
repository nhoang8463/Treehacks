from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

"""form to let existing user to login"""
class LoginForm(FlaskForm):
    username = StringField('User Name')
    password = PasswordField('Password')
    login = SubmitField('Login')


"""form to let a user register an account"""
class RegisterForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
