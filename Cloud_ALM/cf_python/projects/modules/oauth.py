import sys
import requests
import json
import os

credentials = {
    "auth_server_url": os.getenv('api_token_url'),
    "client_id": os.getenv('api_client_id'),
    "client_secret": os.getenv('api_secret')
}


def get_new_token():
    token_req_payload = {'grant_type': 'client_credentials'}
    token_response = requests.post(credentials.auth_server_url,
                                   data=token_req_payload, verify=False, allow_redirects=False,
                                   auth=(credentials.client_id, credentials.client_secret))

    if token_response.status_code != 200:
        print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)

    print("Successfuly obtained a new token")
    tokens = json.loads(token_response.text)
    return tokens['access_token']
