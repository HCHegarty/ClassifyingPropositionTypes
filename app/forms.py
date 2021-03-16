from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class DataEntryForm(FlaskForm):
    text = TextAreaField('Enter Text Here', validators=[DataRequired()])
    submit = SubmitField('Classify Text')