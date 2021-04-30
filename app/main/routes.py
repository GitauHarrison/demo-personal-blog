from app import db, stripe_keys
from flask import render_template, url_for, flash, redirect, request, \
    jsonify, g, current_app
from app.models import User, ArticlesList, PersonalBlogPost, VagrantPost, \
    VirtualenvwrapperPost, reCaptchaPost, richTextPost, ngrokPost, \
    installDocker, HerokuDeployment, WebDevelopmentPost, HelloWorldPost, \
    FlaskTemplatesPost, FlaskWebFormsPost, FlaskDatabasePost, \
    UserCommentsPost, ElasticsearchPost, PortfolioList, FlaskBootstrapPost, \
    DatesAndTimePost, GithubSSHPost, InstallGitPost, FileUploadsPost,\
    StripeInFlaskPost, WhatsappChatbotPost, TwilioSendGridPost, TOTP2faPost,\
    TwilioVerifyPost, TwilioAuthyPost, SimpleVideoAppPost
import stripe
from guess_language import guess_language
from app.translate import translate
from flask_babel import get_locale
from app.main.forms import CommentForm, ArticlesForm, PortfolioForm
from app.main import bp
from flask_login import login_required, current_user


@bp.route('/')
@bp.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = ArticlesList.query.order_by(
        ArticlesList.date_posted.desc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.home', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.home', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('home.html',
                           title='Home',
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url
                           )

# ---------------------------------------------------------------
# Updating Articles in Blog
# ---------------------------------------------------------------


@bp.route('/update-blog')
@login_required
def update_blog():
    return render_template('update_blog.html', title='Updating Blog')


@bp.route('/posting-portfolio-projects', methods=['GET', 'POST'])
@login_required
def posting_portfolio_projects():
    form = PortfolioForm()
    if form.validate_on_submit():
        post = PortfolioList(title=form.title.data,
                             overview=form.overview.data,
                             github_link=form.github_link.data,
                             contributor_link=form.contributor_link.data,
                             project_design_link=form.project_design_link.data,
                             live_project_link=form.live_project_link.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.portfolio'))
    page = request.args.get('page', 1, type=int)
    posts = PortfolioList.query.order_by(
        PortfolioList.date_posted.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.portfolio',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.portfolio',
                       page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('posting_portfolio_projects.html',
                           title='Posting Portfolio Projects',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           )


@bp.route('/delete-portfolio-page-projects')
@login_required
def delete_portfolio_page_projects():
    posts = PortfolioList.query.all()
    for post in posts:
        db.session.delete(post)
        db.session.commit()
        flash('Deletion successful: One portfolio project was successfully deleted')
        return redirect(url_for('main.posting_portfolio_projects',
                                _anchor='delete'))
    return render_template('posting_portfolio_projects.html',
                           title='Deleting Portfolio Page Projects')


@bp.route('/posting-home-page-articles', methods=['GET', 'POST'])
@login_required
def posting_home_page_articles():
    form = ArticlesForm()
    if form.validate_on_submit():
        post = ArticlesList(title=form.title.data, content=form.content.data,
                            link=form.link.data
                            )
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.home'))
    page = request.args.get('page', 1, type=int)
    posts = ArticlesList.query.order_by(
        ArticlesList.date_posted.desc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('main.home', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.home', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('posting_home_page_articles.html',
                           title='Posting Home Page Articles',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url
                           )


@bp.route('/delete-home-page-articles')
def delete_home_page_articles():
    posts = ArticlesList.query.all()
    for post in posts:
        db.session.delete(post)
        db.session.commit()
        flash('Deletion successful: One home page post was successfully deleted')
        return redirect(url_for('main.posting_home_page_articles',
                                _anchor='delete'))
    return render_template('posting_home_page_articles.html',
                           title='Delete Home Page Articles'
                           )


# ---------------------------------------------------------------
# Updating Articles in Blog
# ---------------------------------------------------------------


@bp.route('/about-me')
def about_me():
    return render_template('about_me.html', title='About Me')


@bp.route('/hire-me')
def hire_me():
    return render_template('hire_me.html', title='Hire Me')


@bp.route('/my-interests')
def my_interests():
    return render_template('my_interests.html', title='My Interests')


@bp.route('/web-development')
def web_development():
    return render_template('web_development.html', title='Web Development')


# The database to this view function is called WebDevelopmentPost
@bp.route('/getting-started', methods=['GET', 'POST'])
def getting_started():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = WebDevelopmentPost(body=form.comment.data,
                                  author=user,
                                  language=language
                                  )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.getting_started', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = WebDevelopmentPost.query.order_by(
        WebDevelopmentPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.getting_started',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.getting_started',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = WebDevelopmentPost.query.all()
    total = len(all_posts)
    return render_template('getting_started.html',
                           title='Getting Started',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.before_request
def before_request():
    g.locale = str(get_locale())


@bp.route('/portfolio')
def portfolio():
    page = request.args.get('page', 1, type=int)
    posts = PortfolioList.query.order_by(
        PortfolioList.date_posted.desc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.portfolio', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.portfolio', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('portfolio.html',
                           title='Portfolio',
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url
                           )


@bp.route('/portfolio/popup')
def pop_up():
    return render_template('popup.html', title='Pop Up')


@bp.route('/schedule')
def schedule():
    return render_template('schedule_call.html', title='Schedule Call')


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
        # [billing_address_collection] - to display billing address details on
        # the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - capture the payment later
        # [customer_email] - prefill the email input in the form
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the
        # session ID set as a query param
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
    return render_template('stripe_success.html', title='Payment Success')


@bp.route('/cancelled')
def cancelled():
    flash('Sorry, your payment was not successful. Please try making another payment')
    return render_template('stripe_cancel.html', title='Payment Cancelled')


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

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# START OF TUTORIALS
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# ---------------------------------------------------
# Start of Personal Blog Series
# ---------------------------------------------------


@bp.route('/personal-blog', methods=['GET', 'POST'])
def personal_blog():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = PersonalBlogPost(body=form.comment.data,
                                author=user,
                                language=language
                                )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.personal_blog', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = PersonalBlogPost.query.order_by(
        PersonalBlogPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.personal_blog',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.personal_blog',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = PersonalBlogPost.query.all()
    total = len(all_posts)
    return render_template('personal_blog_templates/personal_blog.html',
                           title='Personal Blog',
                           form=form, posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/chapter-1/hello-world', methods=['GET', 'POST'])
def hello_world():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = HelloWorldPost(body=form.comment.data,
                              author=user,
                              language=language
                              )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.hello_world', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = HelloWorldPost.query.order_by(
        HelloWorldPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.hello_world',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.hello_world',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = HelloWorldPost.query.all()
    total = len(all_posts)
    return render_template('personal_blog_templates/hello_world.html',
                           title='Hello World',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/chapter-2/flask-templates', methods=['GET', 'POST'])
def flask_templates():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = FlaskTemplatesPost(body=form.comment.data,
                                  author=user,
                                  language=language
                                  )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.flask_templates', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = FlaskTemplatesPost.query.order_by(
        FlaskTemplatesPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.flask_templates',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.flask_templates',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = FlaskTemplatesPost.query.all()
    total = len(all_posts)
    return render_template('personal_blog_templates/flask_templates.html',
                           title='Flask Templates',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/chapter-3/flask-web-forms', methods=['GET', 'POST'])
def flask_web_forms():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = FlaskWebFormsPost(body=form.comment.data,
                                 author=user,
                                 language=language
                                 )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.flask_web_forms', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = FlaskWebFormsPost.query.order_by(
        FlaskWebFormsPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.flask_web_forms',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.flask_web_forms',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = FlaskWebFormsPost.query.all()
    total = len(all_posts)
    return render_template('personal_blog_templates/flask_web_forms.html',
                           title='Flask Web Forms',
                           form=form, posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/chapter-4/database', methods=['GET', 'POST'])
def flask_database():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = FlaskDatabasePost(body=form.comment.data,
                                 author=user,
                                 language=language
                                 )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.flask_database', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = FlaskDatabasePost.query.order_by(
        FlaskDatabasePost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.flask_database',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.flask_database',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = FlaskDatabasePost.query.all()
    total = len(all_posts)
    return render_template('personal_blog_templates/working_with_database.html',
                           title='Database',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/chapter-5/user-comments', methods=['GET', 'POST'])
def user_comments():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = UserCommentsPost(body=form.comment.data,
                                author=user,
                                language=language
                                )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.user_comments', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = UserCommentsPost.query.order_by(
        UserCommentsPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.user_comments',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.user_comments',
                       _anchor='comments', page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = UserCommentsPost.query.all()
    total = len(all_posts)
    return render_template('personal_blog_templates/user_comments.html',
                           title='User Comments',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/chapter-6/styled-applicatioin', methods=['GET', 'POST'])
def flask_bootstrap():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = FlaskBootstrapPost(body=form.comment.data,
                                  author=user,
                                  language=language
                                  )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.flask_bootstrap', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = FlaskBootstrapPost.query.order_by(
        FlaskBootstrapPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.flask_bootstrap',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.flask_bootstrap',
                       _anchor='comments', page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = UserCommentsPost.query.all()
    total = len(all_posts)
    return render_template('personal_blog_templates/flask_bootstrap.html',
                           title='Styled Application',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/chapter-7/dates-and-time', methods=['GET', 'POST'])
def dates_and_time():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = DatesAndTimePost(body=form.comment.data,
                                author=user,
                                language=language
                                )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.dates_and_time', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = DatesAndTimePost.query.order_by(
            DatesAndTimePost.timestamp.asc()).paginate(
                page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.dates_and_time',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.dates_and_time',
                       _anchor='comments', page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = DatesAndTimePost.query.all()
    total = len(all_posts)
    return render_template('personal_blog_templates/dates_and_time.html',
                           title='Date And Time',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )

# ---------------------------------------------------
# End of Personal Blog Series
# ---------------------------------------------------


@bp.route('/virtualenvwrapper', methods=['GET', 'POST'])
def virtualenvwrapper():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = VirtualenvwrapperPost(body=form.comment.data,
                                     author=user,
                                     language=language
                                     )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.virtualenvwrapper', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = VirtualenvwrapperPost.query.order_by(
        VirtualenvwrapperPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.virtualenvwrapper', _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.virtualenvwrapper',
                       _anchor='comments', page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = VirtualenvwrapperPost.query.all()
    total = len(all_posts)
    return render_template('virtualenvwrapper.html',
                           title='Virtualenvwrapper Tutorial',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/vagrant', methods=['GET', 'POST'])
def vagrant():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = VagrantPost(body=form.comment.data,
                           author=user,
                           language=language
                           )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.vagrant', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = VagrantPost.query.order_by(
        VagrantPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.vagrant',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.vagrant',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = VagrantPost.query.all()
    total = len(all_posts)
    return render_template('vagrant.html',
                           title='Vagrant Tutorial',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/reCaptcha', methods=['GET', 'POST'])
def reCaptcha():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = reCaptchaPost(body=form.comment.data,
                             author=user,
                             language=language
                             )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.reCaptcha', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = reCaptchaPost.query.order_by(
        reCaptchaPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.reCaptcha',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.reCaptcha',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = reCaptchaPost.query.all()
    total = len(all_posts)
    return render_template('reCaptcha.html',
                           title='reCaptcha Tutorial',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/rich-text', methods=['GET', 'POST'])
def rich_text():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = richTextPost(body=form.comment.data,
                            author=user,
                            language=language
                            )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.rich_text', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = richTextPost.query.order_by(
        richTextPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.rich_text', _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.rich_text',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = richTextPost.query.all()
    total = len(all_posts)
    return render_template('rich_text.html',
                           title='Rich Text Tutorial',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/ngrok', methods=['GET', 'POST'])
def ngrok():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = ngrokPost(body=form.comment.data,
                         author=user,
                         language=language
                         )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.ngrok', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = ngrokPost.query.order_by(
        ngrokPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.ngrok',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.ngrok',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = ngrokPost.query.all()
    total = len(all_posts)
    return render_template('ngrok_tutorial.html',
                           title='Ngrok Tutorial',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/install-docker', methods=['GET', 'POST'])
def install_docker():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = installDocker(body=form.comment.data,
                             author=user,
                             language=language
                             )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.install_docker', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = installDocker.query.order_by(
        installDocker.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.install_docker',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.install_docker',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = installDocker.query.all()
    total = len(all_posts)
    return render_template('install_docker.html',
                           title='Install Docker',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/heroku-deployment', methods=['GET', 'POST'])
def heroku_deployment():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = HerokuDeployment(body=form.comment.data,
                                author=user,
                                language=language
                                )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.heroku_deployment', _anchor='comments'))
    page = request.args.get('page', 1, type=int)
    posts = HerokuDeployment.query.order_by(
        HerokuDeployment.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.heroku_deployment',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.heroku_deployment',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = HerokuDeployment.query.all()
    total = len(all_posts)
    return render_template('heroku_deployment.html',
                           title='Heroku Deployment',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/install-elasticsearch', methods=['GET', 'POST'])
def install_elasticsearch():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = ElasticsearchPost(body=form.comment.data,
                                 author=user,
                                 language=language
                                 )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.install_elasticsearch',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = ElasticsearchPost.query.order_by(
        ElasticsearchPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.install_elasticsearch',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.install_elasticsearch',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = ElasticsearchPost.query.all()
    total = len(all_posts)
    return render_template('elasticsearch.html',
                           title='Install Elasticsearch',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/github_ssh', methods=['GET', 'POST'])
def github_ssh():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = GithubSSHPost(body=form.comment.data,
                             author=user,
                             language=language
                             )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.github_ssh',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = GithubSSHPost.query.order_by(
        GithubSSHPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.github_ssh',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.github_ssh',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = GithubSSHPost.query.all()
    total = len(all_posts)
    return render_template('github_ssh.html',
                           title='GitHub SSH',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/install-git', methods=['GET', 'POST'])
def install_git():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = InstallGitPost(body=form.comment.data,
                              author=user,
                              language=language
                              )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.install_git',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = InstallGitPost.query.order_by(
        InstallGitPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.install_git',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.install_git',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = InstallGitPost.query.all()
    total = len(all_posts)
    return render_template('install_git.html',
                           title='Install Git',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/file-uploads', methods=['GET', 'POST'])
def file_uploads():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = FileUploadsPost(body=form.comment.data,
                               author=user,
                               language=language
                               )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.file_uploads',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = FileUploadsPost.query.order_by(
        FileUploadsPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.file_uploads',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.file_uploads',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = FileUploadsPost.query.all()
    total = len(all_posts)
    return render_template('file_uploads.html',
                           title='File Uploads',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/stripe-in-flask', methods=['GET', 'POST'])
def stripe_in_flask():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = StripeInFlaskPost(body=form.comment.data,
                                 author=user,
                                 language=language
                                 )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.stripe_in_flask',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = StripeInFlaskPost.query.order_by(
        StripeInFlaskPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.stripe_in_flask',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.stripe_in_flask',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = StripeInFlaskPost.query.all()
    total = len(all_posts)
    return render_template('stripe_in_flask.html',
                           title='Stripe In Flask',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/twilio/whatsapp/simple-chatbot', methods=['GET', 'POST'])
def whatsapp_chatbot():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = WhatsappChatbotPost(body=form.comment.data,
                                   author=user,
                                   language=language
                                   )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.whatsapp_chatbot',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = WhatsappChatbotPost.query.order_by(
        WhatsappChatbotPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.whatsapp_chatbot',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.whatsapp_chatbot',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = WhatsappChatbotPost.query.all()
    total = len(all_posts)
    return render_template('chatbot/simple_chatbot.html',
                           title='WhatsApp Chatbot',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/twilio/sendgrid', methods=['GET', 'POST'])
def twilio_sendgrid():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = TwilioSendGridPost(body=form.comment.data,
                                  author=user,
                                  language=language
                                  )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.twilio_sendgrid',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = TwilioSendGridPost.query.order_by(
        TwilioSendGridPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.twilio_sendgrid',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.twilio_sendgrid',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = TwilioSendGridPost.query.all()
    total = len(all_posts)
    return render_template('twilio_sendgrid.html',
                           title='Twilio SendGrid',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )

# -----------------------
# Two-factor Authentication
# -----------------------


@bp.route('/2fa/totp', methods=['GET', 'POST'])
def totp_2fa():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = TOTP2faPost(body=form.comment.data,
                           author=user,
                           language=language
                           )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.totp_2fa',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = TOTP2faPost.query.order_by(
        TOTP2faPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.totp_2fa',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.totp_2fa',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = TOTP2faPost.query.all()
    total = len(all_posts)
    return render_template('2fa/totp.html',
                           title='TOTP 2fa',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/2fa/twilio-verify', methods=['GET', 'POST'])
def twilio_verify():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = TwilioVerifyPost(body=form.comment.data,
                                author=user,
                                language=language
                                )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.twilio_verify',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = TwilioVerifyPost.query.order_by(
        TwilioVerifyPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.twilio_verify',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.twilio_verify',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = TwilioVerifyPost .query.all()
    total = len(all_posts)
    return render_template('2fa/twilio_verify.html',
                           title='Optional 2fa',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


@bp.route('/2fa/twilio-authy', methods=['GET', 'POST'])
def twilio_authy():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = TwilioAuthyPost(body=form.comment.data,
                               author=user,
                               language=language
                               )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.twilio_authy',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = TwilioAuthyPost.query.order_by(
        TwilioAuthyPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.twilio_authy',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.twilio_authy',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = TwilioAuthyPost .query.all()
    total = len(all_posts)
    return render_template('2fa/twilio_authy.html',
                           title='Push Notification',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )

# -----------------------
# End of Two-factor Authentication
# -----------------------

# -----------------------
# Twilio Video App
# -----------------------


@bp.route('/video/simple-video-app', methods=['GET', 'POST'])
def simple_video_app():
    form = CommentForm()
    if form.validate_on_submit():
        language = guess_language(form.comment.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        user = User(username=form.username.data, email=form.email.data)
        post = SimpleVideoAppPost(body=form.comment.data,
                                  author=user,
                                  language=language
                                  )
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('main.simple_video_app',
                                _anchor='comments'
                                )
                        )
    page = request.args.get('page', 1, type=int)
    posts = SimpleVideoAppPost.query.order_by(
        SimpleVideoAppPost.timestamp.asc()).paginate(
            page, current_app.config['POSTS_PER_PAGE'], False
        )
    next_url = url_for('main.simple_video_app',
                       _anchor='comments',
                       page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.simple_video_app',
                       _anchor='comments',
                       page=posts.prev_num) \
        if posts.has_prev else None
    all_posts = SimpleVideoAppPost .query.all()
    total = len(all_posts)
    return render_template('video_app/simple_video_app.html',
                           title='Simple Video App',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url,
                           total=total
                           )


# -----------------------
# End of Twilio Video App
# -----------------------

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# END OF TUTORIALS
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
