# Required Modules
import json
import requests
# from requests_oauth2client import OAuth2Client
import os
import dotenv

VATSIM_AUTH = os.getenv('VATSIM_AUTH_ENDPOINT') + '/oauth/token'

VATSIM_CLIENT_ID = os.getenv('VATSIM_AUTH_CLIENT_ID')
VATSIM_CLIENT_SECRET = os.getenv('VATSIM_AUTH_CLIENT_SECRET')
userData = 'https://api.zfwartcc.net/user?id='

# oauth2client = OAuth2Client(
#     tokenEndpoint = VATSIM_AUTH,
#     auth = (VATSIM_CLIENT_ID, VATSIM_CLIENT_SECRET)
# )

# Fetch user data from server
def getUserData(cid):
    rawData = requests.get(userData + str(cid))
    jsonData = json.loads(rawData.text)

    return jsonData


ddTest = getUserData(1223849)
print(userData + str(1223849))
print(ddTest)