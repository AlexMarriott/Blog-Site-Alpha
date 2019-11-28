"""
This file contains all of the configuration values for the application.
Update this file with the values for your specific Google Cloud project.
You can create and manage projects at https://console.developers.google.com
"""

import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = os.urandom(24)

# There are three different ways to store the data in the application.
# You can choose 'datastore', 'cloudsql', or 'mongodb'. Be sure to
# configure the respective settings for the one you choose below.
# You do not have to configure the other data backends. If unsure, choose
# 'datastore' as it does not require any additional configuration.
DATA_BACKEND = 'datastore'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'eighth-road-254709'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  'details.json'
#GOOGLE_OAUTH2_CLIENT_ID = \
#    '810944511239-occbhvd31l29h5q4mgs85805ogd01ang.apps.googleusercontent.com'
#GOOGLE_OAUTH2_CLIENT_SECRET = 'jiEQbjPib3XdSwaVv5tTNo2F'
GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'
os.environ['GOOGLE_DISCOVERY_URL'] = GOOGLE_DISCOVERY_URL
#Test app client
GOOGLE_CLIENT_ID = '810944511239-3h62gr2jlmont1qt6ok7ts7v1t805ae4.apps.googleusercontent.com'
os.environ['GOOGLE_CLIENT_ID'] = GOOGLE_CLIENT_ID
#Secret
GOOGLE_CLIENT_SECRET = '5TW0496uPJdeZG4Sdfx4bGC3'
os.environ['GOOGLE_CLIENT_SECRET'] = GOOGLE_CLIENT_SECRET
