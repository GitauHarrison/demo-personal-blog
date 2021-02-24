from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired

# from app.models import User
from flask_pagedown.fields import PageDownField
from flask_ckeditor import CKEditorField


class CommentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    comment = PageDownField('Comment', validators=[DataRequired()], \
                            render_kw={"placeholder": "Markdown Enabled"})
    recaptcha = RecaptchaField('Captcha')
    submit = SubmitField('Post')


class ArticlesForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = CKEditorField('Article Content', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()], \
                       render_kw={"placeholder": "Use URL not view function"})
    submit = SubmitField('Post')


class PortfolioForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    # file = FileField('Project Image', render_kw={"class": "dropzone"})
    file = FileField('Project Image', validators=[FileRequired()])
    overview = CKEditorField('Project Details', validators=[DataRequired()])
    github_link = StringField('GitHub Project Link', validators=[DataRequired()], render_kw={"placeholder": "Use GitHub URL"})
    contributor_link = StringField('Contributor', validators=[DataRequired()], render_kw={"placeholder": "Use URL"})
    project_design_link = StringField('Project Design', validators=[DataRequired()], render_kw={"placeholder": "Use URL"})
    live_project_link = StringField('Live Project', validators=[DataRequired()], render_kw={"placeholder": "Use URL"})
    submit = SubmitField('Post')
