# Required Modules
import json
import requests
# from requests_oauth2client import OAuth2Client
import os
from dotenv import load_dotenv
import httplib

load_dotenv()
VATSIM_AUTH = os.getenv('VATSIM_AUTH_ENDPOINT')
USER_DATA_URL = 'https://api.zfwartcc.net/user?id='

def getAuthToken():
    CLIENT_ID = os.getenv('VATSIM_AUTH_CLIENT_ID')
    CLIENT_SECRET = os.getenv('VATSIM_AUTH_CLIENT_SECRET')
    TOKEN_URL = VATSIM_AUTH + '/oauth/token'

    conn = httplib.HTTPSConnection(VATSIM_AUTH)

    url = "/oauth/token"

    params = {
        "grant type": "client_credentials"
    }

# Fetch user data from server
def getUserData(cid):
    rawData = requests.get(USER_DATA_URL + str(cid))
    jsonData = json.loads(rawData.text)

    return jsonData


ddTest = getUserData(1223849)
print(USER_DATA_URL + str(1223849))
print(ddTest)