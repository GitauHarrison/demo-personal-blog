from flask import render_template, current_app
from app.email import send_email


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
