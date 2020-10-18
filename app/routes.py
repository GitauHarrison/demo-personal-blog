from app import app
from flask import render_template, url_for

@app.route('/about_me')
def about_me():
    return render_template('about_me.html', title = 'About Me')

@app.route('/hire_me')
def hire_me():
    return render_template('hire_me.html', title = 'Hire Me')