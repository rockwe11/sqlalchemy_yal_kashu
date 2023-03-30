from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField("Время работы", validators=[DataRequired()])
    collaborators = StringField("Список id участников", validators=[DataRequired()])
    category = IntegerField("Id категории работы", validators=[DataRequired()])
    is_finished = BooleanField("Завершена")
    submit = SubmitField('Применить')
