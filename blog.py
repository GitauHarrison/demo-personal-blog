from app import app, db
from app.models import User, PersonalBlogPost, VagrantPost, VirtualenvwrapperPost, reCaptchaPost

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'PersonalBlogPost': PersonalBlogPost, 'VagrantPost': VagrantPost, 'VirtualenvwrapperPost': VirtualenvwrapperPost, \
         'reCaptchaPost': reCaptchaPost
    }