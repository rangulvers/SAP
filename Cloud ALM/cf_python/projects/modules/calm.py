import modules.oauth as oauth
import requests


def get_projects(token):

    api_call_headers = {'Authorization': 'Bearer ' + token}
    api_call_response = requests.get(
        get_projects_api, headers=api_call_headers)
    if api_call_response.status_code == 401:
        token = oauth.get_new_token()
    else:
        print(api_call_response)

    return api_call_response.text


def get_tasks(token, projectid):

    api_call_headers = {'Authorization': 'Bearer ' + token}
    api_call_response = requests.get(
        get_tasks_api, headers=api_call_headers)
    if api_call_response.status_code == 401:
        token = oauth.get_new_token()
    else:
        print(api_call_response)

    return api_call_response.text
