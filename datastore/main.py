"""
from flask import Flask, redirect, url_for
from flask_login import LoginManager, login_required
from API.model_datastore import get_user
from google.cloud import storage
from config import bucketName, bucketFolder
import config


def create_app(config_class=config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    return app

app = create_app(config)

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucketName)

@login_required
@app.route('/upload_image/<file>')
def upload_image(file):

    if not file:
        return None
#    public_url = storage.upload_file(
        file.read(),
        file.filename,
        file.content_type
    )

    return public_url

def

#if __name__ == '__main__':
#    application.run(host='127.0.0.1', port='5000',  debug=True, ssl_context='adhoc')
"""