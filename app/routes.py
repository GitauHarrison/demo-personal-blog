from app import app, db, stripe_keys
from flask import render_template, url_for, flash, redirect, request, jsonify
from app.forms import CommentForm
from app.models import User, Post
import stripe
from guess_language import guess_language
from app.translate import translate

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html', title = 'About Me')

@app.route('/hire-me')
def hire_me():
    return render_template('hire_me.html', title = 'Hire Me')

@app.route('/my-interests')
def my_interests():
    return render_template('my_interests.html', title = 'My Interests')

@app.route('/web-development')
def web_development():
    return render_template('web_development.html', title = 'Web Development')

@app.route('/personal-blog', methods = ['GET', 'POST'])
def personal_blog():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username = form.username.data, email = form.email.data)        
        post = Post(body = form.comment.data, author = user, language = language)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')  
        return redirect(url_for('personal_blog', _anchor='comments'))  
    page = request.args.get('page', type = int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('personal_blog', _anchor='comments', page = posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('personal_blog', _anchor='comments', page = posts.prev_num) \
        if posts.has_prev else None
    return render_template('personal_blog.html', title = 'Personal Blog', form = form, posts = posts.items, next_url = next_url, prev_url = prev_url)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title = 'Portfolio')

@app.route('/schedule')
def schedule():
    return render_template('schedule_call.html', title = 'Schedule Call')

# START OF STRIPE PAYMENT INTEGRATION
@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://localhost:5000/"
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
                    "amount": "20000",
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403

@app.route('/success')
def success():
    flash('You have successfuly made your payment. Check out more course contents')
    return render_template('stripe_success.html', title = 'Payment Success')

@app.route('/cancelled')
def cancelled():
    flash('Sorry, your payment was not successful. Please try making another payment')
    return render_template('stripe_cancel.html', title = 'Payment Cancelled')

@app.route("/webhook", methods=["POST"])
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
@app.route('/translate')
def translate_text():
    return jsonify({
        'text': translate(
            request.form['text'],
            request.form['source_language'],
            request.form['dest_language']
        )
    })
# END OF LIVE TRANSLATION

# START OF TUTORIALS
@app.route('/virtualenvwrapper')
def virtualenvwrapper():
    return render_template('virtualenvwrapper.html', title = 'Virtualenvwrapper')