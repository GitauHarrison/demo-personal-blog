from app import db
from datetime import datetime
from hashlib import md5
from markdown import markdown
import bleach


class ArticlesList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True)
    date_posted = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    content = db.Column(db.String(), index=True)
    link = db.Column(db.String(140), index=True)


class PortfolioList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), index=True)
    date_posted = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    overview = db.Column(db.String(), index=True)
    github_link = db.Column(db.String(140), index=True)
    contributor_link = db.Column(db.String(140), index=True)
    project_design_link = db.Column(db.String(300), index=True)
    live_project_link = db.Column(db.String(140), index=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    posts = db.relationship('PersonalBlogPost',
                            backref='author',
                            lazy='dynamic'
                            )
    vagrant_posts = db.relationship('VagrantPost',
                                    backref='author',
                                    lazy='dynamic'
                                    )
    virtualenvwrapper_posts = db.relationship('VirtualenvwrapperPost',
                                              backref='author',
                                              lazy='dynamic'
                                              )
    reCaptcha_posts = db.relationship('reCaptchaPost',
                                      backref='author',
                                      lazy='dynamic'
                                      )
    rich_text_posts = db.relationship('richTextPost',
                                      backref='author',
                                      lazy='dynamic'
                                      )
    ngrok_posts = db.relationship('ngrokPost',
                                  backref='author',
                                  lazy='dynamic'
                                  )
    docker_installation_posts = db.relationship('installDocker',
                                                backref='author',
                                                lazy='dynamic'
                                                )
    heroku_deployment = db.relationship('HerokuDeployment',
                                        backref='author',
                                        lazy='dynamic'
                                        )
    web_development = db.relationship('WebDevelopmentPost',
                                      backref='author',
                                      lazy='dynamic'
                                      )
    github_ssh = db.relationship('GithubSSHPost',
                                 backref='author',
                                 lazy='dynamic'
                                 )
    install_git = db.relationship('InstallGitPost',
                                  backref='author',
                                  lazy='dynamic'
                                  )
    file_uploads = db.relationship('FileUploadsPost',
                                   backref='author',
                                   lazy='dynamic'
                                   )
    stripe_in_flask = db.relationship('StripeInFlaskPost',
                                      backref='author',
                                      lazy='dynamic'
                                      )
    whatsapp_chatbot = db.relationship('WhatsappChatbotPost',
                                       backref='author',
                                       lazy='dynamic'
                                       )
    twilio_sendgrid = db.relationship('TwilioSendGridPost',
                                      backref='author',
                                      lazy='dynamic'
                                      )
    totp_2fa = db.relationship('TOTP2faPost',
                               backref='author',
                               lazy='dynamic'
                               )
    twilio_verify = db.relationship('TwilioVerifyPost',
                                    backref='author',
                                    lazy='dynamic'
                                    )

    # Start of Personal Blog Tutorial
    hello_world = db.relationship('HelloWorldPost',
                                  backref='author',
                                  lazy='dynamic'
                                  )
    flask_templates = db.relationship('FlaskTemplatesPost',
                                      backref='author',
                                      lazy='dynamic'
                                      )
    flask_web_forms = db.relationship('FlaskWebFormsPost',
                                      backref='author',
                                      lazy='dynamic')
    flask_databases = db.relationship('FlaskDatabasePost',
                                      backref='author',
                                      lazy='dynamic'
                                      )
    user_comments = db.relationship('UserCommentsPost',
                                    backref='author',
                                    lazy='dynamic'
                                    )
    elasticsearch_comments = db.relationship('ElasticsearchPost',
                                             backref='author',
                                             lazy='dynamic'
                                             )
    flask_bootstrap = db.relationship('FlaskBootstrapPost',
                                      backref='author',
                                      lazy='dynamic'
                                      )
    dates_and_time = db.relationship('DatesAndTimePost',
                                     backref='author',
                                     lazy='dynamic'
                                     )
    # End of Personal Blog Tutorial

    def __repr__(self):
        return 'User: {}'.format(self.username)

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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Comment: {}'.format(self.body)


db.event.listen(PersonalBlogPost.body,
                'set',
                PersonalBlogPost.on_changed_body
                )


class ElasticsearchPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post {}'.format(self.body)


db.event.listen(ElasticsearchPost.body,
                'set',
                ElasticsearchPost.on_changed_body
                )


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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(VagrantPost.body,
                'set',
                VagrantPost.on_changed_body
                )


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
        return 'Post: {}'.format(self.body)


db.event.listen(VirtualenvwrapperPost.body,
                'set',
                VirtualenvwrapperPost.on_changed_body
                )


class reCaptchaPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(reCaptchaPost.body,
                'set',
                reCaptchaPost.on_changed_body
                )


class richTextPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(richTextPost.body,
                'set',
                richTextPost.on_changed_body
                )


class ngrokPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(ngrokPost.body,
                'set',
                ngrokPost.on_changed_body
                )


class installDocker(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(installDocker.body,
                'set',
                installDocker.on_changed_body
                )


class HerokuDeployment(db.Model):
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
        return 'Post: {}'.format(self.body)


db.event.listen(HerokuDeployment.body,
                'set',
                HerokuDeployment.on_changed_body
                )


class WebDevelopmentPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(WebDevelopmentPost.body,
                'set',
                WebDevelopmentPost.on_changed_body
                )


class GithubSSHPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(GithubSSHPost.body,
                'set',
                GithubSSHPost.on_changed_body
                )


class InstallGitPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(InstallGitPost.body,
                'set',
                InstallGitPost.on_changed_body
                )


class FileUploadsPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(FileUploadsPost.body,
                'set',
                FileUploadsPost.on_changed_body
                )


class StripeInFlaskPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(StripeInFlaskPost.body,
                'set',
                StripeInFlaskPost.on_changed_body
                )


class WhatsappChatbotPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(WhatsappChatbotPost.body,
                'set',
                WhatsappChatbotPost.on_changed_body
                )


class TwilioSendGridPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(TwilioSendGridPost.body,
                'set',
                TwilioSendGridPost.on_changed_body
                )


class TOTP2faPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(TOTP2faPost.body,
                'set',
                TOTP2faPost.on_changed_body
                )


class TwilioVerifyPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(TwilioVerifyPost.body,
                'set',
                TwilioVerifyPost.on_changed_body
                )

# -----------------------
# Personal Blog
# -----------------------


class HelloWorldPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(HelloWorldPost.body,
                'set',
                HelloWorldPost.on_changed_body
                )


class FlaskTemplatesPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(FlaskTemplatesPost.body,
                'set',
                FlaskTemplatesPost.on_changed_body
                )


class FlaskWebFormsPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(FlaskWebFormsPost.body,
                'set',
                FlaskWebFormsPost.on_changed_body
                )


class FlaskDatabasePost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(FlaskDatabasePost.body,
                'set',
                FlaskDatabasePost.on_changed_body
                )


class UserCommentsPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(UserCommentsPost.body,
                'set',
                UserCommentsPost.on_changed_body
                )


class FlaskBootstrapPost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(FlaskBootstrapPost.body,
                'set',
                FlaskBootstrapPost.on_changed_body
                )


class DatesAndTimePost(db.Model):
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
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'), tags=allowed_tags, strip=True))

    def __repr__(self):
        return 'Post: {}'.format(self.body)


db.event.listen(DatesAndTimePost.body,
                'set',
                DatesAndTimePost.on_changed_body
                )

# -----------------------
# End of Personal Blog
# -----------------------
