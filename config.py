"""
This file contains all of the configuration values for the application.
Update this file with the values for your specific Google Cloud project.
You can create and manage projects at https://console.developers.google.com
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


# google storage details.
bucketName = 'badgcloudstorage'
os.environ['GCP_BUCKET_NAME'] = bucketName
os.environ['CLOUD_STORAGE_BUCKET'] = bucketName
CLOUD_STORAGE_BUCKET =bucketName
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'eighth-road-254709'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'
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

#mail rest
mail_rest_key = '5c6e63da526366dc3b48d02f7f63b3f0'
mail_rest_secret = 'e6c0fc180d27257c1cdf00df0ac48b95'

os.environ['mail_rest_key'] = mail_rest_key
os.environ['mail_rest_secret'] = mail_rest_secret

#Trello

#API key
trello_api_key='6dfdcbf567aa3c277da8698223bd0fd8'
#Token
trello_secret='3837feb309aa5b57be8780155be9573010f487ea7ebf54a39ddd0195cd5367c6'

os.environ['trello_api_key'] = trello_api_key
os.environ['trello_secret'] = trello_secret