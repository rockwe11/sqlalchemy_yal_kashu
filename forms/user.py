from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    city_from = StringField('Родной город', validators=[DataRequired()])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = StringField('Профессия', validators=[DataRequired()])
    address = StringField("Адрес", validators=[DataRequired()])
    submit = SubmitField('Войти')
