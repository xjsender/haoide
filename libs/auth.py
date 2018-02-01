'''
Inspired by requests_oauth2
'''

from .. import requests
from urllib.parse import quote,urlencode

import hmac
import hashlib
import base64

class SalesforceOAuth2(object):
    authorization_url = '/services/oauth2/authorize'
    token_url = '/services/oauth2/token'
    revoke_url = '/services/oauth2/revoke'

    def __init__(self, client_id, client_secret, redirect_uri, login_url="https://test.salesforce.com", **kwargs):
        self.auth_site = login_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def _request_token(self, data):
        url = "{site}{token_url}".format(
            site=self.auth_site, token_url=self.token_url)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        post_data = {'client_id': self.client_id,
                     'client_secret': self.client_secret}
        post_data.update(data)
        result = requests.post(url, data=post_data, headers=headers, verify=False)
        return result, result.json()

    def authorize_url(self, **kwargs):
        
        # scope = kwargs.get('scope', quote('full refresh_token'))
        # fields = {
        #     'site': self.auth_site,
        #     'authorize_url': self.authorization_url,
        #     'clientid': self.client_id,
        #     'redirect_uri': quote(self.redirect_uri),
        #     'scope': scope
        # }

        # return "{site}{authorize_url}?response_type=code&client_id={clientid}&redirect_uri={redirect_uri}&scope={scope}".format(**fields)
        fields = {
            'response_type': 'token',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'prompt': 'login',
            'display': 'popup'
        }
        url = self.auth_site + self.authorization_url + '?' + urlencode(fields)

        return url

    def get_token(self, code):
        data = {
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri,
            'code': code
        }
        response, response_json = self._request_token(data)
        if 'access_token' in response_json:
            self.access_token = response_json['access_token']
        if 'refresh_token' in response_json:
            self.refresh_token = response_json['refresh_token']
        return response_json

    def refresh_token(self, refresh_token):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }
        response, response_json = self._request_token(data)

        if 'access_token' in response_json:
            self.access_token = response_json['access_token']
        return response_json

    def generate_signature(self, id, issued_at):
        data = "{id}{issued}".format(id=id, issued=issued_at)
        digest = hmac.new(
            self.client_secret, data, digestmod=hashlib.sha256).digest()
        return base64.b64encode(digest).decode()

    def revoke_token(self, current_token):
        # Perform a GET request, because that's by far the easiest way
        url = "{site}{revoke_url}".format(
            site=self.auth_site, revoke_url=self.revoke_url)
        data = {
            'token': quote(current_token)
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        return requests.post(url, data=data, headers=headers, verify=False)
