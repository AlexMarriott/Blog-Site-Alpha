from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class SlackForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Send Message')

class EmailForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email_address = StringField('Email', validators=[Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    note = TextAreaField('Note', validators=[DataRequired(), Length(min=2, max=200)])

    submit = SubmitField('Send Email')
