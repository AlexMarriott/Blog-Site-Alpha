import datetime

from flask import Blueprint, render_template, redirect, url_for,Flask,request
from google.auth.transport import requests
from google.cloud import datastore
import google.oauth2.id_token
main = Blueprint('main', __name__)
firebase_request_adapter = requests.Request()


@main.route('/')
def root():
    return render_template('index.html')

@main.route('/index')
def index():
    return redirect(url_for('main.root'))

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/signin')
def sign_in():
    return render_template('signin.html')

@main.route('/signout')
def sign_out():
        # Verify Firebase auth.
        id_token = request.cookies.get("token")
        error_message = None
        claims = None
        times = None

        if id_token:
            try:
                # Verify the token against the Firebase Auth API. This example
                # verifies the token on each page load. For improved performance,
                # some applications may wish to cache results in an encrypted
                # session store (see for instance
                # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
                claims = google.oauth2.id_token.verify_firebase_token(
                    id_token, firebase_request_adapter)
            except ValueError as exc:
                # This will be raised if the token is expired or any other
                # verification checks fail.
                error_message = str(exc)

            # Record and fetch the recent times a logged-in user has accessed
            # the main. This is currently shared amongst all users, but will be
            # individualized in a following step.
            times = datetime.datetime.now()

        return render_template(
            'signin.html',
            user_data=claims, error_message=error_message, times=times)
