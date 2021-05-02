from flask import render_template, url_for, flash, request, redirect,\
    session
from werkzeug.urls import url_parse
from app import db
from app.auth import bp
from app.models import Admin
from flask_login import current_user, login_user, logout_user,\
    login_required
from app.auth.forms import RegistrationForm, LoginForm,\
    RequestPasswordResetForm, ResetPasswordForm, Enable2faForm,\
    Confirm2faForm, Disable2faForm
from app.auth.email import send_password_reset_email
from app.auth.twilio_verify import request_verification_token,\
    check_verification_token


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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.admin')
        if admin.two_factor_enabled():
            request_verification_token(admin.verification_phone)
            session['username'] = admin.username
            session['phone'] = admin.verification_phone
            return redirect(url_for(
                'auth.verify_2fa', next=next_page,
                remember='1' if form.remember_me.data else '0'))
        login_user(admin, remember=form.remember_me.data)
        return redirect(next_page)
    return render_template('admin/auth/login.html',
                           title='Login',
                           form=form
                           )


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


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

# 2fa


@bp.route('/enable_2fa', methods=['GET', 'POST'])
@login_required
def enable_2fa():
    form = Enable2faForm()
    if form.validate_on_submit():
        session['phone'] = form.verification_phone.data
        request_verification_token(session['phone'])
        return redirect(url_for('auth.verify_2fa'))
    return render_template('admin/auth/enable_2fa.html',
                           form=form,
                           title='Enable 2FA'
                           )


@bp.route('/verify2fa', methods=['GET', 'POST'])
def verify_2fa():
    form = Confirm2faForm()
    if form.validate_on_submit():
        phone = session['phone']
        if check_verification_token(phone, form.token.data):
            del session['phone']
            if current_user.is_authenticated:
                current_user.verification_phone = phone
                db.session.commit()
                flash('Two-factor authentication is now enabled')
                return redirect(url_for('auth.login'))
            else:
                username = session['username']
                del session['username']
                user = Admin.query.filter_by(username=username).first()
                next_page = request.args.get('next')
                remember = request.args.get('remember', '0') == '1'
                login_user(user, remember=remember)
                return redirect(next_page)
        form.token.errors.append('Invalid token')
    return render_template('admin/auth/verify_2fa.html',
                           form=form,
                           title='Verify 2fa'
                           )


@bp.route('/disable_2fa', methods=['GET', 'POST'])
@login_required
def disable_2fa():
    form = Disable2faForm()
    if form.validate_on_submit():
        current_user.verification_phone = None
        db.session.commit()
        flash('Two-factor authentication is now disabled')
        return redirect(url_for('auth.login'))
    return render_template('admin/auth/disable_2fa.html',
                           form=form,
                           title='Disable 2fa'
                           )
