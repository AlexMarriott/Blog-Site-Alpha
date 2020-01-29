import datetime
import six
from flask import current_app
from werkzeug.exceptions import BadRequest
from google.cloud import storage

import os
'''
Template file upload code used from googles example code set :https://github.com/GoogleCloudPlatform/getting-started-python/blob/797d153f1b63684e4a2069158788f774a98d5b02/3-binary-data/bookshelf/storage.py
This is the main interface for uploading files to google storage.
'''

def _get_storage_client():
    return storage.Client(
        project=current_app.config['PROJECT_ID'])


def _check_extension(filename, allowed_extensions):
    if ('.' not in filename or
            filename.split('.').pop().lower() not in allowed_extensions):
        raise BadRequest(
            "{0} has an invalid name or extension".format(filename))


def _safe_filename(filename):
    """
    Generates a safe filename that is unlikely to collide with existing objects
    in Google Cloud Storage.

    ``filename.ext`` is transformed into ``filename-YYYY-MM-DD-HHMMSS.ext``
    """
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
    basename, extension = filename.rsplit('.', 1)
    return "{0}-{1}.{2}".format(basename, date, extension)


# [START upload_file]
def upload_file(file_stream, filename, content_type):
    """
    Uploads a file to a given Cloud Storage bucket and returns the public url
    to the new object.
    """
    _check_extension(filename, current_app.config['ALLOWED_EXTENSIONS'])
    des_filename = _safe_filename(filename)



    client = _get_storage_client()
    try:
        client.get_bucket(os.environ['CLOUD_STORAGE_BUCKET'])

    except Exception as e:
        print(e)
        created_bucket = client.create_bucket(os.environ['CLOUD_STORAGE_BUCKET'])

    bucket = client.get_bucket(os.environ['CLOUD_STORAGE_BUCKET'])

    blob = bucket.blob(des_filename)

    blob.upload_from_string(
        file_stream,
        content_type=content_type)

    url = blob.public_url

    if isinstance(url, six.binary_type):
        url = url.decode('utf-8')

    return url

