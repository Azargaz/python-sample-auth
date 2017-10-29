"""sample_graphrest.py - graphrest sample for Microsoft Graph"""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import os

import bottle
import graphrest

from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
MSGRAPH = graphrest.GraphSession(client_id=CLIENT_ID,
                                 client_secret=CLIENT_SECRET,
                                 redirect_uri=REDIRECT_URI,
                                 scopes=['User.Read'])

bottle.TEMPLATE_PATH = ['./static/templates']

@bottle.route('/')
@bottle.view('homepage.html')
def homepage():
    """Render the home page."""
    return {'sample': 'graphrest'}

@bottle.route('/login')
def login():
    """Prompt user to authenticate."""
    MSGRAPH.login()

@bottle.route('/login/authorized')
def authorized():
    """Handler for the application's Redirect Uri."""
    MSGRAPH.get_token(redirect_to='/graphcall')

@bottle.route('/graphcall')
@bottle.view('graphcall.html')
def graphcall():
    """Confirm user authentication by calling Graph and displaying some data."""
    endpoint = 'me'
    graphdata = MSGRAPH.get(endpoint).json()
    return {'graphdata': graphdata,
            'endpoint': MSGRAPH.api_endpoint(endpoint),
            'sample': 'graphrest'}

@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    """Static dev/test file server"""
    static_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
    return bottle.static_file(filepath, root=static_root)

if __name__ == '__main__':
    bottle.run(app=bottle.app(), server='wsgiref', host='localhost', port=5000)