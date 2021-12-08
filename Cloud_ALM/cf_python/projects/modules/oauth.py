import sys
import requests
import json


def get_new_token(eauth_server_url, eclient_id, eclient_secret):
    auth_server_url = eauth_server_url
    client_id = eclient_id
    client_secret = eclient_secret

    token_req_payload = {'grant_type': 'client_credentials'}

    token_response = requests.post(auth_server_url,
                                   data=token_req_payload, verify=False, allow_redirects=False,
                                   auth=(client_id, client_secret))

    if token_response.status_code != 200:
        print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)

    print("Successfuly obtained a new token")
    tokens = json.loads(token_response.text)
    return tokens['access_token']
