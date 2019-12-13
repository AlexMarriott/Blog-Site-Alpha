
import os

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from .forms import SlackForm, EmailForm
from mailjet_rest import Client

import json
import time
import requests

main = Blueprint('main', __name__)


def get_channel_messages():
    # 1575565009.378274
    channel_data = json.loads(requests.get(

        'https://slack.com/api/channels.history?token=xoxp-847971877056-847971877792-847997585669-c8a17eca7c3853fa0fa4b558461d5774&channel=CQLEU7DMZ&latest={0}&count=5&pretty=1'.format(
            time.time())).text)
    channel_messages = {}
    j = 0
    for i in channel_data['messages']:
        j += 1
        channel_messages[j] = i['text']
    return channel_messages


@main.route('/slack/channel_msg', methods=['GET'])
def get_latest_message():
    # 1575565009.378274
    channel_data = json.loads(requests.get(
        'https://slack.com/api/channels.history?token=xoxp-847971877056-847971877792-847997585669-c8a17eca7c3853fa0fa4b558461d5774&channel=CQLEU7DMZ&latest={0}&inclusive=true&count=1pretty=1'.format(
            time.time())).text)
    return channel_data['messages'][0]['text']

@main.route('/index')
@main.route('/')
def root():
    return redirect(url_for('blog.blog_index'))

@main.route('/contact', methods=['POST', 'GET'])
@login_required
def contact():
    email_form = EmailForm()
    slack_form = SlackForm()
    if email_form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        try:
            if [data['email_address'], data['name'], data['subject'], data['note']] is not None:
                try:
                    mailjet = Client(auth=(os.environ['mail_rest_key'], os.environ['mail_rest_secret']), version='v3.1')
                    data = {
                        'Messages': [
                            {
                                "From": {
                                    "Email": 'pinkconsole362@gmail.com',
                                    "Name": "Blog Site Alpha User: {0} says".format(data['name'])
                                },
                                "To": [
                                    {
                                        "Email": "pinkconsole362@gmail.com",
                                        "Name": "Alex"
                                    }
                                ],
                                "Subject": data['subject'],
                                "TextPart": "Sent message: {0} ..... \n Senders email: {1}".format(data['subject'], data['email_address']),
                                "HTMLPart": "Sent message: {0} ..... \n Senders email: {1}".format(data['subject'], data['email_address']),
                                "CustomID": "User Email"
                            }
                        ]
                    }
                    result = mailjet.send.create(data=data)
                    print(result.status_code)
                    print(result.json())
                except Exception as e:
                    print(e)
                    flash(e, 'danger')
                    return render_template('contact.html', action='main.contact', slack_form=slack_form,
                                           email_form=email_form,
                                           slack_messages=get_channel_messages())
                flash('Email sent!', 'info')
                return render_template('contact.html', action='main.contact', slack_form=slack_form,
                                       email_form=email_form,
                                       slack_messages=get_channel_messages())
            else:
                flash('Please fill out all fields in the email form.', 'warning')
                return render_template('contact.html', action='main.contact', slack_form=slack_form,
                                       email_form=email_form,
                                       slack_messages=get_channel_messages())
        except KeyError as e:
            print(e)
            flash(e, 'error')
            return render_template('contact.html', action='main.contact', slack_form=slack_form, email_form=email_form,
                                   slack_messages=get_channel_messages())
    elif slack_form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        if data['message'] is not None:
            # post to slack
            try:
                resp = requests.post(
                    'https://hooks.slack.com/services/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', json={
                        'text': '{0} @ {1} says: {2}'.format(current_user.name, current_user.email,
                                                             data['message'])})
                if resp.status_code == 200:
                    print('Message sent!')
                else:
                    print('error, message was not sent')
                    print(resp.status_code)
                    print(resp.text)
            except Exception as e:
                print(e)
                flash(e, 'warning')
                return render_template('contact.html', action='main.contact', slack_form=slack_form,
                                       email_form=email_form,
                                       slack_messages=get_channel_messages())
        else:
            pass
    # Reads all the messages in the website-chat channel
    return render_template('contact.html', action='main.contact', slack_form=slack_form, email_form=email_form,
                           slack_messages=get_channel_messages())



@main.route('/about')
def about():
    return render_template('about.html')


#@login_required
@main.route('/contact/post_to_slack/<message>', methods=['POST'])
def post_slack(message):
        # post to slack
        try:
            resp = requests.post(
                'https://hooks.slack.com/services/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', json={
                    'text': '{0} @ {1} says: {2}'.format(current_user.name, current_user.email,
                                                         message)})
            if resp.status_code == 200:
                flash('Message sent!', 'info')
                return '200'
            else:
                flash('error, message was not sent, {0}'.format(resp.text))
                return '200'
        except Exception as e:
            print(e)
            flash(e, 'warning')
            return '500'
