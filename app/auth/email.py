from flask import render_template, current_app
from app.email import send_email


def send_password_reset_email(admin):
    token = admin.get_reset_password_token()
    send_email(
        '[Password Reset] Personal Blog',
        sender=current_app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('admin/auth/email/reset_password.txt',
                                  admin=admin,
                                  token=token),
        html_body=render_template('admin/auth/email/reset_password.html',
                                  admin=admin,
                                  token=token)
    )
