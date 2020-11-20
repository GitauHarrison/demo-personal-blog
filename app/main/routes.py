from app import db, stripe_keys
from flask import render_template, url_for, flash, redirect, request, jsonify, g, current_app
from app.models import User, PersonalBlogPost,VagrantPost, VirtualenvwrapperPost, reCaptchaPost, richTextPost, ngrokPost, installDocker, HerokuDeployment,\
    WebDevelopmentPost, HelloWorldPost, FlaskTemplatesPost, FlaskWebFormsPost, FlaskDatabasePost
import stripe
from guess_language import guess_language
from app.translate import translate
from flask_babel import get_locale
from app.main.forms import CommentForm
from app.main import bp

@bp.route('/')
@bp.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@bp.route('/about-me')
def about_me():
    return render_template('about_me.html', title = 'About Me')

@bp.route('/hire-me')
def hire_me():
    return render_template('hire_me.html', title = 'Hire Me')

@bp.route('/my-interests')
def my_interests():
    return render_template('my_interests.html', title = 'My Interests')

@bp.route('/web-development', methods = ['GET', 'POST'])
def web_development():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = WebDevelopmentPost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.web_development', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = WebDevelopmentPost.query.order_by(WebDevelopmentPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.web_development', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.web_development', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('web_development.html', title = 'Web Development', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.before_request
def before_request():
    g.locale = str(get_locale())

@bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title = 'Portfolio')

@bp.route('/portfolio/popup')
def pop_up():
    return render_template('popup.html', title = 'Pop Up')

@bp.route('/schedule')
def schedule():
    return render_template('schedule_call.html', title = 'Schedule Call')

# START OF STRIPE PAYMENT INTEGRATION
@bp.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@bp.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "https://gitauharrison-blog.herokuapp.com/"
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - capture the payment later
        # [customer_email] - prefill the email input in the form
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            # success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            success_url=domain_url + "success",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "name": "Consultation",
                    "quantity": 1,
                    "currency": "usd",
                    "amount": "1500",
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403

@bp.route('/success')
def success():
    flash('You have successfuly made your payment. Check out more course contents')
    return render_template('stripe_success.html', title = 'Payment Success')

@bp.route('/cancelled')
def cancelled():
    flash('Sorry, your payment was not successful. Please try making another payment')
    return render_template('stripe_cancel.html', title = 'Payment Cancelled')

@bp.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_keys["endpoint_secret"]
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Payment was successful")
        # TODO: you can run some custom code here

    return "Success", 200
# END OF STRIPE PAYMENT INTEGRATION

# START OF LIVE TRANSLATION
@bp.route('/translate')
def translate_text():
    return jsonify({
        'text': translate(
            request.form['text'],
            request.form['source_language'],
            request.form['dest_language']
        )
    })
# END OF LIVE TRANSLATION

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# START OF TUTORIALS
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#---------------------------------------------------
# Start of Personal Blog Series
#---------------------------------------------------
@bp.route('/personal-blog', methods = ['GET', 'POST'])
def personal_blog():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = PersonalBlogPost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.personal_blog', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = PersonalBlogPost.query.order_by(PersonalBlogPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.personal_blog', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.personal_blog', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('personal_blog_templates/personal_blog.html', title = 'Personal Blog', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/chapter-1/hello-world', methods = ['GET', 'POST'])
def hello_world():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = HelloWorldPost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.hello_world', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = HelloWorldPost.query.order_by(HelloWorldPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.hello_world', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.hello_world', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('personal_blog_templates/hello_world.html', title = 'Hello World', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/chapter-2/flask-templates', methods = ['GET', 'POST'])
def flask_templates():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = FlaskTemplatesPost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.flask_templates', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = FlaskTemplatesPost.query.order_by(FlaskTemplatesPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.flask_templates', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.flask_templates', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('personal_blog_templates/flask_templates.html', title = 'Flask Templates', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/chapter-3/flask-web-forms', methods = ['GET', 'POST'])
def flask_web_forms():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = FlaskWebFormsPost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.flask_web_forms', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = FlaskWebFormsPost.query.order_by(FlaskWebFormsPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.flask_web_forms', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.flask_web_forms', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('personal_blog_templates/flask_web_forms.html', title = 'Flask Web Forms', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/chapter-4/database', methods = ['GET', 'POST'])
def flask_database():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = FlaskDatabasePost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.flask_database', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = FlaskDatabasePost.query.order_by(FlaskDatabasePost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.flask_database', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.flask_database', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('personal_blog_templates/working_with_database.html', title = 'Database', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

#---------------------------------------------------
# End of Personal Blog Series
#---------------------------------------------------

@bp.route('/virtualenvwrapper', methods = ['GET', 'POST'])
def virtualenvwrapper():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = VirtualenvwrapperPost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.virtualenvwrapper', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = VirtualenvwrapperPost.query.order_by(VirtualenvwrapperPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.virtualenvwrapper', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.virtualenvwrapper', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('virtualenvwrapper.html', title = 'Virtualenvwrapper Tutorial', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/vagrant', methods = ['GET', 'POST'])
def vagrant():
    form = CommentForm()
    if form.validate_on_submit():
       language = guess_language(form.comment.data)
       if language == 'UNKNOWN' or len(language) > 5:
           language = ''
       user = User(username = form.username.data, email = form.email.data)        
       post = VagrantPost(body = form.comment.data, author = user, language = language)
       db.session.add(user)
       db.session.add(post)
       db.session.commit()
       flash('Your comment is now live!')  
       return redirect(url_for('main.vagrant', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = VagrantPost.query.order_by(VagrantPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.vagrant', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.vagrant', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('vagrant.html', title = 'Vagrant Tutorial', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/reCaptcha', methods = ['GET', 'POST'])
def reCaptcha():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = reCaptchaPost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.reCaptcha', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = reCaptchaPost.query.order_by(reCaptchaPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.reCaptcha', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.reCaptcha', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('reCaptcha.html', title = 'reCaptcha Tutorial', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/rich-text', methods = ['GET', 'POST'])
def rich_text():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = richTextPost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.rich_text', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = richTextPost.query.order_by(richTextPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.rich_text', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.rich_text', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('rich_text.html', title = 'Rich Text Tutorial', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/ngrok', methods = ['GET', 'POST'])
def ngrok():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = ngrokPost(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.ngrok', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = ngrokPost.query.order_by(ngrokPost.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.ngrok', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.ngrok', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('ngrok_tutorial.html', title = 'Ngrok Tutorial', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/install-docker', methods = ['GET', 'POST'])
def install_docker():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = installDocker(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.install_docker', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = installDocker.query.order_by(installDocker.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.install_docker', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.install_docker', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('install_docker.html', title = 'Install Docker', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@bp.route('/heroku-deployment', methods = ['GET', 'POST'])
def heroku_deployment():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = HerokuDeployment(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('main.heroku_deployment', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = HerokuDeployment.query.order_by(HerokuDeployment.timestamp.asc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.heroku_deployment', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.heroku_deployment', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('heroku_deployment.html', title = 'Heroku Deployment', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# END OF TUTORIALS
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=