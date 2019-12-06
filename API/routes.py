from flask import Flask, request, redirect, Blueprint, render_template
from flask_login import login_required,current_user
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
        #If a card has been submitted, lets create the card.
        if [data['card_title'], data['description']] is not None:
            trello_list = client.get_list('5de9f7c1ba72a567a9bb40d8')
            label = client.get_label(data['label'], '5de9f7c17cf48e47b2e8302d')
            card = Card(data['card_title'], label or '', data['description'], current_user.name, current_user.email)
            resp = trello_list.add_card(name=card.title, desc='{0} \nRequested by: {1}. They can be conected at: {2}'.format(card.description, card.requesting_user, card.requestin_user_email), labels=[label])
            print(resp)
            return render_template('trello.html', action='api.create_trello_card', trello_form=trello_form)
    return render_template('trello.html', action='api.create_trello_card', trello_form=trello_form)
