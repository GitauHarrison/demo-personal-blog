from app import app
from flask import render_template, url_for

@app.route('/about_me')
def about_me():
    return render_template('about_me.html', title = 'About Me')

@app.route('/hire_me')
def hire_me():
    return render_template('hire_me.html', title = 'Hire Me')

@app.route('/my_interests')
def my_interests():
    return render_template('my_interests.html', title = 'My Interests')

@app.route('/web_development')
def web_development():
    return render_template('web_development.html', title = 'Web Development')

@app.route('/personal_blog')
def personal_blog():
    return render_template('personal_blog.html', title = 'Personal Blog')