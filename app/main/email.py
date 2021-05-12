from flask import render_template, current_app
from app.email import send_email


# Hello World

def new_hello_world_comment(admin):
    send_email(
        '[New Comment] Hello World Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/hello_world.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/hello_world.html',
                                  admin=admin)
    )


def send_live_hello_world_email(user):
    send_email(
        '[Your Comment is Live] Hello World Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/hello_world.txt',
                                  user=user),
        html_body=render_template('public_comment_email/hello_world.html',
                                  user=user)
    )


# Flask Templates

def new_flask_templates_comment(admin):
    send_email(
        '[New Comment] Flask Templates Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/flask_templates.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/flask_templates.html',
                                  admin=admin)
    )


def send_live_flask_templates_email(user):
    send_email(
        '[Your Comment is Live] Flask Templates Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/flask_templates.txt',
                                  user=user),
        html_body=render_template('public_comment_email/flask_templates.html',
                                  user=user)
    )


# Flask Web Forms

def new_flask_web_forms_comment(admin):
    send_email(
        '[New Comment] Flask Web Forms Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/flask_web_forms.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/flask_web_forms.html',
                                  admin=admin)
    )


def send_live_flask_web_forms_email(user):
    send_email(
        '[Your Comment is Live] Flask Web Forms Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/flask_web_forms.txt',
                                  user=user),
        html_body=render_template('public_comment_email/flask_web_forms.html',
                                  user=user)
    )


# Flask Database

def new_flask_database_comment(admin):
    send_email(
        '[New Comment] Flask Database Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/flask_database.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/flask_database.html',
                                  admin=admin)
    )


def send_live_flask_database_email(user):
    send_email(
        '[Your Comment is Live] Flask Database Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/flask_database.txt',
                                  user=user),
        html_body=render_template('public_comment_email/flask_database.html',
                                  user=user)
    )


# User Comments

def new_user_comments_comment(admin):
    send_email(
        '[New Comment] User Comment Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/user_comments.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/user_comments.html',
                                  admin=admin)
    )


def send_live_user_comments_email(user):
    send_email(
        '[Your Comment is Live] User Comments Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/user_comments.txt',
                                  user=user),
        html_body=render_template('public_comment_email/user_comments.html',
                                  user=user)
    )


# Flask Bootstrap

def new_flask_bootstrap_comment(admin):
    send_email(
        '[New Comment] Flask Bootstrap Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/flask_bootstrap.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/flask_bootstrap.html',
                                  admin=admin)
    )


def send_live_flask_bootstrap_email(user):
    send_email(
        '[Your Comment is Live] Flask Bootstrap Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/flask_bootstrap.txt',
                                  user=user),
        html_body=render_template('public_comment_email/flask_bootstrap.html',
                                  user=user)
    )


# Dates and Time

def new_dates_and_time_comment(admin):
    send_email(
        '[New Comment] Dates and Time Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/dates_and_time.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/dates_and_time.html',
                                  admin=admin)
    )


def send_live_dates_and_time_email(user):
    send_email(
        '[Your Comment is Live] Dates and Time Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/dates_and_time.txt',
                                  user=user),
        html_body=render_template('public_comment_email/dates_and_time.html',
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
        text_body=render_template('admin/review_comment_email/twilio_sendgrid.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/twilio_sendgrid.html',
                                  admin=admin)
    )


def send_live_twilio_sendgrid_email(user):
    send_email(
        '[Your Comment is Live] Twilio SendGrid Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/twilio_sendgrid.txt',
                                  user=user),
        html_body=render_template('public_comment_email/twilio_sendgrid.html',
                                  user=user)
    )


# TOTP 2FA email

def new_totp_2fa_comment(admin):
    send_email(
        '[New Comment] TOTP 2FA Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/review_comment_email/totp_2fa.txt',
                                  admin=admin),
        html_body=render_template('admin/review_comment_email/totp_2fa.html',
                                  admin=admin)
    )


def send_live_totp_2fa_email(user):
    send_email(
        '[Your Comment is Live] TOTP 2FA Article',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('public_comment_email/totp_2fa.txt',
                                  user=user),
        html_body=render_template('public_comment_email/totp_2fa.html',
                                  user=user)
    )
