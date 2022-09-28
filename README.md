# Personal Blog (Demo)

![GitHub Open Issues](https://img.shields.io/github/issues/GitauHarrison/my-blog) ![GitHub Closed Issues](https://img.shields.io/github/issues-closed/GitauHarrison/my-blog) ![GitHub Pull Request Open](https://img.shields.io/github/issues-pr/GitauHarrison/my-blog) ![GitHub Pull Request Closed](https://img.shields.io/github/issues-pr-closed/GitauHarrison/my-blog) ![GitHub forks](https://img.shields.io/github/forks/GitauHarrison/my-blog) ![GitHub Stars](https://img.shields.io/github/stars/GitauHarrison/my-blog)

![Personal Blog](app/static/images/personal_blog.gif)

### Overview
This is a demo personal blog. I used it to learn how to create a simple flask website from scratch, where I took a note all the projects I was learning by building. It served as a starting point for my learning journey. I now have [my official personal website](https://gitauharrison.com).

### Design
Here is the  [full design](https://www.figma.com/proto/7crZ9XsIKbcptPwzuCxwDJ/Personal-Blog%2FPortfolio?node-id=1%3A2&scaling=min-zoom&page-id=0%3A1) of the blog. I used Figma for prototyping and regular reference during its development.

### Features
* Anonymous user can post comments (even multiple times using the same credentials)
* Realtime Date and Time
* Payment Integration
* Live Language Translation
* Consultation Scheduling
* Database Management
* Markdown Form Editing
* Link Popups
* Comment Moderation
* Two-factor authentication for Admin

### Tools Used

* Calendly for Scheduling
* Microsoft Language Translator
* Flask Framework
* Twitter Bootstrap for Cross-browser Responsiveness
* Python3 for Programming
* SQLite for Local Development
* Stripe For Payment
* Moment JS for Realtime Date and Time
* Gravatar for User Comments
* Google reCaptcha for Extra Form Security
* JQuery for Mobile Responsiveness
* Ngrok for Localhost Testing
* Flask PageDown for form editing
* Twilio Verify

## Application Design

* [Personal Blog Design](https://www.figma.com/proto/7crZ9XsIKbcptPwzuCxwDJ/Personal-Blog%2FPortfolio?node-id=0%3A1&scaling=min-zoom&page-id=0%3A1)

### Contributors:

[![GitHub Contributors](https://img.shields.io/github/contributors/GitauHarrison/my-blog)](https://github.com/GitauHarrison/my-blog/graphs/contributors)


### Deployed Application
* [Gitau Harrison Blog](https://gitauharrison-blog.herokuapp.com/home)  on Heroku
* [Demo Personal Blog](https://demo-personal-blog.onrender.com) - Render

### Testing
To test the project out, you can clone this repo to your local machine:

```python
$ git clone git@github.com:GitauHarrison/my-blog.git
```

Create and activate your virtual environment before running it:
```python
$ workon gitauharrison-portfolio # I am using a virtualenv wrapper
```

Install all used dependancies:
```python
(gitauharrison-portfolio)$ pip3 install -r requirements.txt
```

Run the application:
```python
$ flask run
```
Once your application is running, you can access your `localhost` on http://127.0.0.1:5000/. Additionally, if you look carefully in your terminal, you will see `* Tunnel URL: NgrokTunnel: "http://4209c9af6d43.ngrok.io" -> "http://localhost:5000"`

The `HTTP` value may be different from the one shown here because I am using the free tier package of `ngrok`. Paste the link http://4209c9af6d43.ngrok.io on another device, say your mobile phone, to test the application while it is on `localhost`.

### Build Your Own Blog

A personal blog side project sounds like a great idea. If you would like to learn how you can build your own blog from scratch using Python and Flask, something like the one here, [look here](https://github.com/GitauHarrison/notes/blob/master/web_development/personal_blog/personal_blog.md).

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/GitauHarrison/my-blog)