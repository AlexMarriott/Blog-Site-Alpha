import json

import requests
from flask import Blueprint, render_template, redirect, url_for,request
from flask_login import current_user, login_required

from .forms import SlackForm, EmailForm
main = Blueprint('main', __name__)

@main.route('/')
def root():
    return render_template('index.html')

@main.route('/index')
def index():
    return redirect(url_for('main.root'))

@main.route('/contact', methods=['POST', 'GET'])
@login_required
def contact():
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
                resp = requests.post('https://hooks.slack.com/services/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', json={'text' : '{0} @ {1} says: {2}'.format(current_user.name, current_user.email, data['message'])})
                print(resp)
                print(resp.status_code)
                print(resp.text)
            else:
                pass
    # Reads all the messages in the website-chat channel
    channel_data = json.loads(requests.get('https://slack.com/api/channels.history?token=xoxp-847971877056-847971877792-847997585669-c8a17eca7c3853fa0fa4b558461d5774&channel=CQLEU7DMZ&pretty=1').text)
    channel_messages = []
    for i in channel_data['messages']:
        channel_messages.append(i['text'])
    return render_template('contact.html',action='main.contact', form=form, slack_messages=channel_messages)

@main.route('/about')
def about():
    return render_template('about.html')
