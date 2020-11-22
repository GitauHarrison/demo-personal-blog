from flask import Flask, current_app
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
import stripe
from flask_babel import Babel
from flask_pagedown import PageDown
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
babel = Babel()
pagedown = PageDown()
ckeditor = CKEditor()

stripe_keys = {
        "secret_key": app.config["STRIPE_SECRET_KEY"],
        "publishable_key": app.config["STRIPE_PUBLISHABLE_KEY"],
        "endpoint_secret": app.config["STRIPE_ENDPOINT_SECRET"]
    }

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    migrate.init_app(app, db)
    babel.init_app(app)
    pagedown.init_app(app)
    ckeditor.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
        
    def start_ngrok():
        from pyngrok import ngrok

        url = ngrok.connect(5000)
        print(' * Tunnel URL: ', url)

    if app.config['START_NGROK']:
        start_ngrok()

    if not app.debug:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='noreply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'],
                subject='Gitau Harrison Blog Failure',
                credentials=auth, secure=secure
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler(
                'logs/personal_blog.log',
                maxBytes=10240,
                backupCount=10
            )
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
            ))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
            app.logger.setLevel(logging.INFO)
            app.logger.info('Gitau Harrison Blog')

    return app

@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'en'

from app import models