from trello import TrelloClient
from flask import Flask, request, redirect, Blueprint, render_template
from .forms import TrelloForm
import os

client = TrelloClient(
    api_key=os.environ['trello_api_key'],
    api_secret=os.environ['trello_secret']
)
api = Blueprint('api', __name__)

@api.route('/trello')
def trello():
    trello_form = TrelloForm()
    if trello_form.validate_on_submit():
        data = request.form.to_dict(flat=True)
        if [data['card_title'], data['description']] is not None:
            board = client.get_board('Website-Improvements')
            return render_template('trello.html', action='api.trello', trello_form=trello_form)