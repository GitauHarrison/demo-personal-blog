from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.forms import CommentForm
from app.models import User, Post

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

@app.route('/personal_blog', methods = ['GET', 'POST'])
def personal_blog():
    form = CommentForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)        
        post = Post(body = form.comment.data, author = user)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('personal_blog', _anchor='translate-hover'))  
    page = request.args.get('page', type = int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('personal_blog', _anchor='translate-hover', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('personal_blog', _anchor='translate-hover', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('personal_blog.html', title = 'Personal Blog', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)