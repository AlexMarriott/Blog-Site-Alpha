from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length,Optional

#Nice-to-have: 5de9f7c18bdee58e0d066ce4 , Bug: 5de9f7c18bdee58e0d066ce5 ,
#Need-right-now: 5de9f7c18bdee58e0d066ce7 , Must-have: 5de9f7c18bdee58e0d066ce6
class TrelloForm(FlaskForm):
    card_title = StringField('Title', validators=[DataRequired(), Length(min=1, max=50)])
    description = TextAreaField('Description',validators=[DataRequired(), Length(min=2, max=500)])
    label = SelectField('Label', choices=[('5de9f7c18bdee58e0d066ce4','Nice-to-have'), ('5de9f7c18bdee58e0d066ce6','Must-have'),
                                                        ('5de9f7c18bdee58e0d066ce7','Need-right-now'), ('5de9f7c18bdee58e0d066ce5','Bug')], validators=[Optional()])

    submit = SubmitField('Submit Card')
