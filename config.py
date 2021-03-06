"""Configuration settings for running the Python auth samples locally.

In a production deployment, this information should be saved in a database or
other secure storage mechanism.
"""

CLIENT_ID = 'ENTER_YOUR_CLIENT_ID'
CLIENT_SECRET = 'ENTER_YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:5000/login/authorized'

# AUTHORITY_URL ending determines type of account that can be authenticated:
# /organizations = organizational accounts only
# /consumers = MSAs only (Microsoft Accounts - Live.com, Hotmail.com, etc.)
# /common = allow both types of accounts
AUTHORITY_URL = 'https://login.microsoftonline.com/common'

AUTH_ENDPOINT = '/oauth2/v2.0/authorize'
TOKEN_ENDPOINT = '/oauth2/v2.0/token'

RESOURCE = 'https://graph.microsoft.com/'
API_VERSION = 'v1.0'
SCOPES = ['OnlineMeetings.ReadWrite'] # Add other scopes/permissions as needed.