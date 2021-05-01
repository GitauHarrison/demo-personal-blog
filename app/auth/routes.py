from flask import render_template, url_for, flash, request, redirect
from werkzeug.urls import url_parse
from app import db
from app.auth import bp
from app.models import Admin
from flask_login import current_user, login_user, logout_user
from app.auth.forms import RegistrationForm, LoginForm,\
    RequestPasswordResetForm, ResetPasswordForm
from app.auth.email import send_password_reset_email


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.admin'))
    form = RegistrationForm()
    if form.validate_on_submit():
        admin = Admin(username=form.username.data, email=form.email.data)
        admin.set_password(form.password.data)
        db.session.add(admin)
        db.session.commit()
        flash('You are now an admin of this blog')
        return redirect(url_for('auth.login'))
    return render_template('admin/auth/register.html',
                           title='Admin',
                           form=form
                           )


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.admin'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=form.username.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(admin, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.admin')
        return redirect(next_page)
    return render_template('admin/auth/login.html',
                           title='Login',
                           form=form
                           )


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@bp.route('/request-password-reset', methods=['GET', 'POST'])
def request_password_reset():
    if current_user.is_authenticated:
        return redirect(url_for('main.admin'))
    form = RequestPasswordResetForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin:
            send_password_reset_email(admin)
        flash('Check your email for instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('admin/auth/request_password_reset.html',
                           title='Request Password Reset',
                           form=form
                           )


@bp.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.admin'))
    admin = Admin.verify_reset_password_token(token)
    if not admin:
        return redirect(url_for('main.home'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        admin.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset')
        return redirect(url_for('auth.login'))
    return render_template('admin/auth/reset_password.html',
                           title='Reset Password',
                           form=form
                           )
