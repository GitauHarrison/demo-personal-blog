from flask import render_template, current_app
from app.email import send_email


# Hello World

def new_hello_world_comment(admin):
    send_email(
        '[New Comment] Hello World Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/personal_blog/hello_world.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/personal_blog/hello_world.html',
                                  admin=admin)
    )


def send_live_hello_world_email(user):
    send_email(
        '[Your Comment is Live] Hello World Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/personal_blog/hello_world.txt',
                                  user=user),
        html_body=render_template('public_comment_email/personal_blog/hello_world.html',
                                  user=user)
    )


# Flask Templates

def new_flask_templates_comment(admin):
    send_email(
        '[New Comment] Flask Templates Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/personal_blog/flask_templates.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/personal_blog/flask_templates.html',
                                  admin=admin)
    )


def send_live_flask_templates_email(user):
    send_email(
        '[Your Comment is Live] Flask Templates Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/personal_blog/flask_templates.txt',
                                  user=user),
        html_body=render_template('public_comment_email/personal_blog/flask_templates.html',
                                  user=user)
    )


# Flask Web Forms

def new_flask_web_forms_comment(admin):
    send_email(
        '[New Comment] Flask Web Forms Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/personal_blog/flask_web_forms.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/personal_blog/flask_web_forms.html',
                                  admin=admin)
    )


def send_live_flask_web_forms_email(user):
    send_email(
        '[Your Comment is Live] Flask Web Forms Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/personal_blog/flask_web_forms.txt',
                                  user=user),
        html_body=render_template('public_comment_email/personal_blog/flask_web_forms.html',
                                  user=user)
    )


# Flask Database

def new_flask_database_comment(admin):
    send_email(
        '[New Comment] Flask Database Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/personal_blog/flask_database.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/personal_blog/flask_database.html',
                                  admin=admin)
    )


def send_live_flask_database_email(user):
    send_email(
        '[Your Comment is Live] Flask Database Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/personal_blog/flask_database.txt',
                                  user=user),
        html_body=render_template('public_comment_email/personal_blog/.html',
                                  user=user)
    )


# User Comments

def new_user_comments_comment(admin):
    send_email(
        '[New Comment] User Comment Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/personal_blog/user_comments.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/personal_blog/user_comments.html',
                                  admin=admin)
    )


def send_live_user_comments_email(user):
    send_email(
        '[Your Comment is Live] User Comments Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/personal_blog/user_comments.txt',
                                  user=user),
        html_body=render_template('public_comment_email/personal_blog/user_comments.html',
                                  user=user)
    )


# Flask Bootstrap

def new_flask_bootstrap_comment(admin):
    send_email(
        '[New Comment] Flask Bootstrap Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/personal_blog/flask_bootstrap.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/personal_blog/flask_bootstrap.html',
                                  admin=admin)
    )


def send_live_flask_bootstrap_email(user):
    send_email(
        '[Your Comment is Live] Flask Bootstrap Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/personal_blog/flask_bootstrap.txt',
                                  user=user),
        html_body=render_template('public_comment_email/personal_blog/flask_bootstrap.html',
                                  user=user)
    )


# Dates and Time

def new_dates_and_time_comment(admin):
    send_email(
        '[New Comment] Dates and Time Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/personal_blog/dates_and_time.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/personal_blog/dates_and_time.html',
                                  admin=admin)
    )


def send_live_dates_and_time_email(user):
    send_email(
        '[Your Comment is Live] Dates and Time Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/personal_blog/dates_and_time.txt',
                                  user=user),
        html_body=render_template('public_comment_email/personal_blog/dates_and_time.html',
                                  user=user)
    )


# Virtualeenvwrapper

def new_virtualenvwrapper_comment(admin):
    send_email(
        '[New Comment] Virtualenvwrapper Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/virtualenvwrapper.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/virtualenvwrapper.html',
                                  admin=admin)
    )


def send_live_virtualenvwrapper_email(user):
    send_email(
        '[Your Comment is Live] Virtualenvwrapper Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/virtualenvwrapper.txt',
                                  user=user),
        html_body=render_template('public_comment_email/virtualenvwrapper.html',
                                  user=user)
    )


# GitHub SSH

def new_github_ssh_comment(admin):
    send_email(
        '[New Comment] GitHub SSH Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/github_ssh.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/github_ssh.html',
                                  admin=admin)
    )


def send_live_github_ssh_email(user):
    send_email(
        '[Your Comment is Live] GitHub SSH Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/github_ssh.txt',
                                  user=user),
        html_body=render_template('public_comment_email/github_ssh.html',
                                  user=user)
    )


# Install Git Email

def new_install_git_comment(admin):
    send_email(
        '[New Comment] Install Git Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/install_git.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/install_git.html',
                                  admin=admin)
    )


def send_live_install_git_email(user):
    send_email(
        '[Your Comment is Live] Install Git Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/install_git.txt',
                                  user=user),
        html_body=render_template('public_comment_email/install_git.html',
                                  user=user)
    )


# Getting Started Email

def new_getting_started_comment(admin):
    send_email(
        '[New Comment] Getting Started Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/getting_started.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/getting_started.html',
                                  admin=admin)
    )


def send_live_getting_started_email(user):
    send_email(
        '[Your Comment is Live] Getting Started Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/getting_started.txt',
                                  user=user),
        html_body=render_template('public_comment_email/getting_started.html',
                                  user=user)
    )


# Twilio SendGrid Email

def new_twilio_sendgrid_comment(admin):
    send_email(
        '[New Comment] Twilio SendGrid Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/twilio/twilio_sendgrid.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/twilio/twilio_sendgrid.html',
                                  admin=admin)
    )


def send_live_twilio_sendgrid_email(user):
    send_email(
        '[Your Comment is Live] Twilio SendGrid Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/twilio/twilio_sendgrid.txt',
                                  user=user),
        html_body=render_template('public_comment_email/twilio/twilio_sendgrid.html',
                                  user=user)
    )


# TOTP 2FA email

def new_totp_2fa_comment(admin):
    send_email(
        '[New Comment] TOTP 2FA Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/2fa/totp_2fa.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/2fa/totp_2fa.html',
                                  admin=admin)
    )


def send_live_totp_2fa_email(user):
    send_email(
        '[Your Comment is Live] TOTP 2FA Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/2fa/totp_2fa.txt',
                                  user=user),
        html_body=render_template('public_comment_email/2fa/totp_2fa.html',
                                  user=user)
    )


# Vargrant

def new_vagrant_comment(admin):
    send_email(
        '[New Comment] Vagrant Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/vagrant.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/vagrant.html',
                                  admin=admin)
    )


def send_live_vagrant_email(user):
    send_email(
        '[Your Comment is Live] Vagrant Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/vagrant.txt',
                                  user=user),
        html_body=render_template('public_comment_email/vagrant.html',
                                  user=user)
    )


# Install Docker

def new_install_docker_comment(admin):
    send_email(
        '[New Comment] Install Docker Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/install_docker.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/install_docker.html',
                                  admin=admin)
    )


def send_live_install_docker_email(user):
    send_email(
        '[Your Comment is Live] Install Docker Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/install_docker.txt',
                                  user=user),
        html_body=render_template('public_comment_email/install_docker.html',
                                  user=user)
    )


# Elasticsearch

def new_elasticsearch_comment(admin):
    send_email(
        '[New Comment] Elasticsearch Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/elasticsearch.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/elasticsearch.html',
                                  admin=admin)
    )


def send_live_elasticsearch_email(user):
    send_email(
        '[Your Comment is Live] Elasticsearch Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/elasticsearch.txt',
                                  user=user),
        html_body=render_template('public_comment_email/elasticsearch.html',
                                  user=user)
    )


# Ngrok

def new_ngrok_comment(admin):
    send_email(
        '[New Comment] Ngrok Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/ngrok.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/ngrok.html',
                                  admin=admin)
    )


def send_live_ngrok_email(user):
    send_email(
        '[Your Comment is Live] Ngrok Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/ngrok.txt',
                                  user=user),
        html_body=render_template('public_comment_email/ngrok.html',
                                  user=user)
    )


# reCaptcha

def new_reCaptcha_comment(admin):
    send_email(
        '[New Comment] reCaptcha Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/reCaptcha.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/reCaptcha.html',
                                  admin=admin)
    )


def send_live_reCaptcha_email(user):
    send_email(
        '[Your Comment is Live] reCaptcha Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/reCaptcha.txt',
                                  user=user),
        html_body=render_template('public_comment_email/reCaptcha.html',
                                  user=user)
    )


# Rich Text

def new_rich_text_comment(admin):
    send_email(
        '[New Comment] Rich Text Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/rich_text.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/rich_text.html',
                                  admin=admin)
    )


def send_live_rich_text_email(user):
    send_email(
        '[Your Comment is Live] Rich Text Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/rich_text.txt',
                                  user=user),
        html_body=render_template('public_comment_email/rich_text.html',
                                  user=user)
    )


# Heroku Deployment

def new_heroku_deployment_comment(admin):
    send_email(
        '[New Comment] Heroku Deployment Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/heroku_deployement.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/heroku_deployement.html',
                                  admin=admin)
    )


def send_live_heroku_deployment_email(user):
    send_email(
        '[Your Comment is Live] Heroku Deployment Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/heroku_deployement.txt',
                                  user=user),
        html_body=render_template('public_comment_email/heroku_deployement.html',
                                  user=user)
    )


# Stripe

def new_stripe_comment(admin):
    send_email(
        '[New Comment] Stripe Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/stripe.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/stripe.html',
                                  admin=admin)
    )


def send_live_stripe_email(user):
    send_email(
        '[Your Comment is Live] Stripe Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/stripe.txt',
                                  user=user),
        html_body=render_template('public_comment_email/stripe.html',
                                  user=user)
    )
