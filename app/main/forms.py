from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
# from app.models import User
from flask_pagedown.fields import PageDownField
from flask_ckeditor import CKEditorField

class CommentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    comment = PageDownField('Comment', validators=[DataRequired()], render_kw={"placeholder": "Markdown Enabled"})
    recaptcha = RecaptchaField('Captcha')
    submit = SubmitField('Post')

class ArticlesForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = CKEditorField('Article Content', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()], render_kw={"placeholder": "Use URL not view function"})
    submit = SubmitField('Post')