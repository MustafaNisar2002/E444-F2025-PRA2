# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

class NameEmailForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    email = StringField("UofT email", validators=[DataRequired(), Email()])
    submit = SubmitField("Submit")

    def validate_email(self, field):
        # PRA requirement: ensure a UofT address (contains "utoronto")
        if "utoronto" not in field.data.lower():
            raise ValidationError('Please use a UofT email address (contains "utoronto").')
