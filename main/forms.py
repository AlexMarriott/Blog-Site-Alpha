from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SlackForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Send Message')

class EmailForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email_address = StringField('Email', validators=[Email()])
    message = TextAreaField('Comment', validators=[DataRequired(), Length(min=2, max=200)])

    submit = SubmitField('Send Email')
