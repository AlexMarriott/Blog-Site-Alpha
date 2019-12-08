from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)])
    post_data = TextAreaField('PostData',validators=[DataRequired(), Length(min=10, max=500)])
    picture = FileField()
    submit = SubmitField('Submit Post')

class Comment(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired(), Length(min=2, max=200)])

    submit = SubmitField('Submit Comment')