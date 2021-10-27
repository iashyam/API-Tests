import os
from google.auth.transport import Request
import google_auth_oauthlib
import googleapiclient.discovery
import googleapiclient.errors
import json as j
# from httplib2 import Response

API_NAME ='youtube'
API_VERSION = 'v3'
CLINT_SECRET_FILE = 'client_secret_332754604906-8giefi3jkk52hv0hn8fh0m329tfpn9lo.apps.googleusercontent.com.json'

scopes =['https://www.googleapis.com/auth/youtube.readonly']

channel_id = 'UCIxZHDq5tql4ejYtqYLTtxQ'
mine = True

flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file( CLINT_SECRET_FILE, scopes)

crendentails = flow.run_console()

# print(crendentails)

youtube = googleapiclient.discovery.build(API_NAME, API_VERSION,credentials=crendentails)

Request = youtube.channels().list(
    part='contentDetails',
    id = channel_id
)

Response = Request.execute()

with open('response.json', 'w') as f:
    j.dump(Response,f)

