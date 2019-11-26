import requests
from flask import Blueprint, render_template, redirect, url_for,request
from flask_login import current_user

from .forms import SlackForm, EmailForm
main = Blueprint('main', __name__)

@main.route('/')
def root():
    return render_template('index.html',current_user=current_user)

@main.route('/index')
def index():
    return redirect(url_for('main.root'))

@main.route('/contact', methods=['POST', 'GET'])
def contact(email=None, message=None):
    form = SlackForm()
    #xoxp-847971877056-847971877792-847997585669-c8a17eca7c3853fa0fa4b558461d5774 <- access token to slack
    if form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        try:
            if data['email'] is not None:
                #Do some stuff with email
                pass
        except KeyError:
            if data['message'] is not None:
                #post to slack
                #curl -X POST -H 'Content-type: application/json'
                #--data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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
                print(message)
                resp = requests.post('https://hooks.slack.com/services/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', json={'text':data['message']})
                print(resp)
                print(resp.status_code)
                print(resp.text)
            else:
                pass
    return render_template('contact.html',action='main.contact', form=form)

@main.route('/about')
def about():
    return render_template('about.html')
