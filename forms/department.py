from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField('Название департамента', validators=[DataRequired()])
    members = StringField("Список id участников", validators=[DataRequired()])
    email = StringField("Почта департамента", validators=[DataRequired()])
    submit = SubmitField('Добавить')
