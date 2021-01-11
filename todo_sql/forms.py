from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    id = IntegerField("id", validators=[DataRequired()])
    nazwa = StringField("nazwa", validators=[DataRequired()])
    deadline = TextAreaField("deadline", validators=[DataRequired()])
    priorytet = SelectField("priorytet", choices=['bardzo ważne', 'ważne', 'śrenioważne', 'opcjonalne'])
