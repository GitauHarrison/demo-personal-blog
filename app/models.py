from app import db
from datetime import datetime
from hashlib import md5
from markdown import markdown
import bleach

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    posts = db.relationship('PersonalBlogPost', backref='author', lazy='dynamic')
    vagrant_posts = db.relationship('VagrantPost', backref='author', lazy='dynamic')
    virtualenvwrapper_posts = db.relationship('VirtualenvwrapperPost', backref='author', lazy='dynamic')

    def __repr__(self):
        return 'User <>'.format(self.username)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

class PersonalBlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    body_html = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) 
    language = db.Column(db.String(5))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = [
            'a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
            'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
            'h1', 'h2', 'h3', 'p'
        ]
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format = 'html'), tags = allowed_tags, strip = True))
        
    def __repr__(self):
        return 'Post <>'.format(self.body)
        
db.event.listen(PersonalBlogPost.body, 'set', PersonalBlogPost.on_changed_body)

class VagrantPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    body_html = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) 
    language = db.Column(db.String(5))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = [
            'a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
            'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
            'h1', 'h2', 'h3', 'p'
        ]
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format = 'html'), tags = allowed_tags, strip = True))
        
    def __repr__(self):
        return 'Post <>'.format(self.body)
        
db.event.listen(VagrantPost.body, 'set', VagrantPost.on_changed_body)

class VirtualenvwrapperPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    body_html = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)     
    language = db.Column(db.String(5))    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = [
            'a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
            'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
            'h1', 'h2', 'h3', 'p'
        ]
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format = 'html'), tags = allowed_tags, strip = True))
        
    def __repr__(self):
        return 'Post <>'.format(self.body)
        
db.event.listen(VirtualenvwrapperPost.body, 'set', VirtualenvwrapperPost.on_changed_body)