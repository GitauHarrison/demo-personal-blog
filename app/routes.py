from app import app
from flask import render_template, url_for

@app.route('/about_me')
def about_me():
    return render_template('about_me.html', title = 'About Me')