# I Am Found Here 100% of The Time

![Personal Blog](app/static/images/personal_blog.png)

### Overview
This is my blog, where I note all the projects I am involved in, my personal interests and other aspects of life I am engaged in.

### Design
Here is the  [full design](https://www.figma.com/proto/7crZ9XsIKbcptPwzuCxwDJ/Personal-Blog-Portfolio?node-id=1%3A2&scaling=min-zoom) of the blog. I used Figma for prototyping and regualar reference during its development.

# Features
* User Authentication
* Functional Password Reset Feature
* Ability to post comments
* Realtime Date and Time
* Database Management
* Extra form protection
* Autofocus of the Chat Input Box
* Use of the Enter Key to Send Message
* Descent Automatic Chat Page Scrolldown
* Pre-created Rooms
* Immediate Addition of User in Default Room
* Chat Privacy in All Rooms
* Tools Used
* Flask Framework
* Flask SocketIO
* Twitter Bootstrap for Cross-browser Responsiveness
* Python3 for Programming
* Javascript for Extra Page Interactivity
* SQLite for Local Development
* Python Datetime Module for Localtime Management
* Moment JS for Improved Time Formatting
* Google reCaptcha for Extra Form Security
* JQuery for Mobile Responsiveness
* Ngrok for Localhost Testing

### Contributors:
* [Gitau Harrison](https://github.com/GitauHarrison)

### Deployed Application
* [Gitau Harrison Blog on Heroku](https://gitauharrison-blog.herokuapp.com/home)

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
$ pip3 install -r requirements.txt
```

Run the application:
```python
$ flask run
```
Once your application is running, you can access your `localhost` on http://127.0.0.1:5000/. Additionally, if you look carefully in your terminal, you will see `* Tunnel URL: NgrokTunnel: "http://4209c9af6d43.ngrok.io" -> "http://localhost:5000"`

The `HTTP` value may be different from the one shown here because I am using the free tier package of `ngrok`. Paste the link http://4209c9af6d43.ngrok.io on another device, say your mobile phone, to test the application while it is on `localhost`.