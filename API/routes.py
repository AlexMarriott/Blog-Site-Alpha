from flask import Flask, request, redirect, Blueprint, render_template
from .forms import TrelloForm
from .models import Card
import os
import trello

client = trello.TrelloClient(
    api_key=os.environ['trello_api_key'],
    api_secret=os.environ['trello_secret']
)

api = Blueprint('api', __name__)


@api.route('/trello', methods=['POST', 'GET'])
def create_trello_card():
    trello_form = TrelloForm()
    if trello_form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        print(data)
        if [data['card_title'], data['description']] is not None:
            #TODO use the current logged in user.
            trello_list = client.get_list('5de9f7c1ba72a567a9bb40d8')
            card = Card(data['card_title'], data['label'] or '', data['description'], 'test_user')
            resp = trello_list.add_card(name=card.title, desc='{0} \nRequested by: {1}'.format(card.description,card.requesting_user, label=card.label))
            print(resp.labels)
            return render_template('trello.html', action='api.create_trello_card', trello_form=trello_form)

    return render_template('trello.html', action='api.create_trello_card', trello_form=trello_form)