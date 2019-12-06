from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class TrelloForm(FlaskForm):
    card_title = StringField('Title', validators=[DataRequired(), Length(min=1, max=50)])
    description = TextAreaField('Description',validators=[DataRequired(), Length(min=2, max=500)])
    labels = StringField('Label', validators=[DataRequired(), Length(min=1, max=50)])

    submit = SubmitField('Submit Card')
