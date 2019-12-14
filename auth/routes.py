import requests
import os
import json
from API.models import User
from API.model_datastore import create_user, get_user
from flask import Blueprint, request, redirect, url_for, session
from flask_login import (
    login_required,
    login_user,
    logout_user
)
from oauthlib.oauth2 import WebApplicationClient

"""
Google Oauth is templated from https://realpython.com/flask-google-login/
The auth blueprint is used for logging in the user and handling the users session.

"""
auth = Blueprint('auth', __name__)
client = WebApplicationClient(os.environ['GOOGLE_CLIENT_ID'])

@auth.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=fix_http(request.base_url) + "/callback",
        scope=["openid", "email", "profile"],
    )
    session['url'] = request.referrer
    return redirect(request_uri)

def fix_http(request_url):
    import re
    new_url = re.sub(
        "http:",
        "https:",
        request_url
    )
    return new_url
@auth.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=fix_http(request.url),
        redirect_url=fix_http(request.base_url),
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(os.environ['GOOGLE_CLIENT_ID'],os.environ['GOOGLE_CLIENT_SECRET']),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens (yay) let's find and hit URL
    # from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, authorized our
    # app, and now we've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in our db with the information provided
    # by Google
    user = User(
        id=unique_id, name=users_name, email=users_email, profile_pic=picture
    )
    # Doesn't exist? Add to database
    if not get_user(unique_id):
        create_user(user)

    # Begin user session by logging the user in
    login_user(user)
    session['user'] = user.convert_to_dict()
    

    # Send user back to homepage
    try:
        return_url = session['url'] or "/"
    except KeyError as e:
        print(e)
        return_url = '/'
    return redirect(return_url)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    del session['user']
    return redirect(url_for("main.root"))


def get_google_provider_cfg():
    return requests.get(os.environ['GOOGLE_DISCOVERY_URL']).json()
