from flask import Flask, request, redirect, Blueprint, render_template
from .forms import TrelloForm
from .models import Card
import os
import trello

client = trello.TrelloClient(
    api_key=os.environ['trello_api_key'],
    api_secret=os.environ['trello_secret']
)
#board = trello..get_board('5de9f7c17cf48e47b2e8302d')
#trello_list = client.('5de9f7c1ba72a567a9bb40d8')

api = Blueprint('api', __name__)

@api.route('/trello')
def trello():
    trello_form = TrelloForm()
    if trello_form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        if [data['card_title'], data['description']] is not None:
            #TODO use the current logged in user.
            card = Card(data['title'], data['label'] or '', data['description'], 'test_user')
            #client.
            return render_template('trello.html', action='api.trello', trello_form=trello_form)