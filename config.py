"""
This file contains all of the configuration values for the application.
Update this file with the values for your specific Google Cloud project.

"""

import os
#TODO see if the env variables can be put into a different folder.

#The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = os.urandom(24)

# There are three different ways to store the data in the application.
# You can choose 'datastore', 'cloudsql', or 'mongodb'. Be sure to
# configure the respective settings for the one you choose below.
# You do not have to configure the other data backends. If unsure, choose
# 'datastore' as it does not require any additional configuration.
DATA_BACKEND = 'datastore'


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'
# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'eighth-road-254709'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
