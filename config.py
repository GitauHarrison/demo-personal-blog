import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # Form security
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database configuration
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    # Pagination
    POSTS_PER_PAGE=3

    # Email configuration
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT='587'
    MAIL_USE_TLS='True'
    MAIL_USERNAME='tastebolder@gmail.com'
    MAIL_PASSWORD=b"\xafO'n\xa8T\xae\xff\x9bGXvT\xfd\xa2\x9d"
    ADMINS=['norulesanymore@gmail.com']

    # Stripe
    STRIPE_PUBLISHABLE_KEY='pk_test_51HedKjKExJxw7LdpAQR3oWJ1AWW94e8leKDmjbPkLbjvW81NzX2jXntzt774lnSxiuubyBItFVPUmeVUsxBWaoNH00eLRpQz3v'
    STRIPE_SECRET_KEY='sk_test_51HedKjKExJxw7LdpBoS4e5v2Bekry7MvxSCXjKKBjchSe59n9KADKBJzwiFqLxIFEstnY8V1Mn6BYm00hQET99Wl00lEhu0Lj5'
    STRIPE_ENDPOINT_SECRET='whsec_wnJMeZIAWSHZm5sONh5eBP8pSmiWpcDp'

    # MS Live Translation
    MS_TRANSLATOR_KEY='344435f010f8410caaa6c1f972507a3e'

    # Manual Translation Language Options
    LANGUAGES=['en', 'sw']

    # reCAPTCHA configuration
    RECAPTCHA_PUBLIC_KEY='6LfLJN8ZAAAAAJgBHQy76zPyHVR2O9jmaTThPTLP'
    RECAPTCHA_PRIVATE_KEY='6LfLJN8ZAAAAACe28iK98cDOBl-1REobjjR-em1a'

    # Ngrok configuration
    START_NGROK=os.environ.get('START_NGROK') is not None and \
        os.environ.get('WERKZEUG_RUN_MAIN') is not 'true'

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')