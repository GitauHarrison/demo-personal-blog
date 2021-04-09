from app import create_app, db
from app.models import ArticlesList, User, PersonalBlogPost, VagrantPost, \
     VirtualenvwrapperPost, reCaptchaPost, richTextPost, ngrokPost, \
     installDocker, HerokuDeployment, WebDevelopmentPost, HelloWorldPost, \
     FlaskTemplatesPost, FlaskWebFormsPost, FlaskDatabasePost, \
     UserCommentsPost, ElasticsearchPost, PortfolioList, DatesAndTimePost, \
     FlaskBootstrapPost, GithubSSHPost, InstallGitPost, FileUploadsPost,\
     StripeInFlaskPost, WhatsappChatbotPost, TwilioSendGridPost, TOTP2faPost,\
     TwilioVerifyPost, TwilioAuthyPost


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'ArticlesList': ArticlesList,
            'User': User,
            'PersonalBlogPost': PersonalBlogPost,
            'VagrantPost': VagrantPost,
            'VirtualenvwrapperPost': VirtualenvwrapperPost,
            'reCaptchaPost': reCaptchaPost,
            'richTextPost': richTextPost,
            'ngrokPost': ngrokPost,
            'installDocker': installDocker,
            'HerokuDeployment': HerokuDeployment,
            'WebDevelopmentPost': WebDevelopmentPost,
            'HelloWorldPost': HelloWorldPost,
            'FlaskTemplatesPost': FlaskTemplatesPost,
            'FlaskWebFormsPost': FlaskWebFormsPost,
            'FlaskDatabasePost': FlaskDatabasePost,
            'UserCommentsPost': UserCommentsPost,
            'ElasticsearchPost': ElasticsearchPost,
            'PortfolioList': PortfolioList,
            'DatesAndTimePost': DatesAndTimePost,
            'FlaskBootstrapPost': FlaskBootstrapPost,
            'GithubSSHPost': GithubSSHPost,
            'InstallGitPost': InstallGitPost,
            'FileUploadsPost': FileUploadsPost,
            'StripeInFlaskPost': StripeInFlaskPost,
            'WhatsappChatbotPost': WhatsappChatbotPost,
            'TwilioSendGridPost': TwilioSendGridPost,
            'TOTP2faPost': TOTP2faPost,
            'TwilioVerifyPost': TwilioVerifyPost,
            'TwilioAuthyPost': TwilioAuthyPost
            }
