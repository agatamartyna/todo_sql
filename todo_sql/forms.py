from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    id = StringField("id")
    nazwa = StringField("nazwa", validators=[DataRequired()])
    deadline = TextAreaField("deadline", validators=[DataRequired()])
    priorytet = SelectField(
        "priorytet",
        choices=['bardzo ważne', 'ważne', 'śrenioważne', 'opcjonalne'])
