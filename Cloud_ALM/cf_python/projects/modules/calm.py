import modules.oauth as oauth
import requests
import os


def get_projects(token):
    get_projects_api = os.getenv('api_url_projects')
    api_call_headers = {'Authorization': 'Bearer ' + token}
    api_call_response = requests.get(
        get_projects_api, headers=api_call_headers)
    if api_call_response.status_code == 401:
        token = oauth.get_new_token()
    else:
        print(api_call_response)

    return api_call_response.text


def get_tasks(token, projectid):
    get_tasks_api = os.getenv('api_url_tasks').join(f"?projectId={projectid}")
    print(get_tasks_api)
    api_call_headers = {'Authorization': 'Bearer ' + token}
    api_call_response = requests.get(
        get_tasks_api, headers=api_call_headers)
    if api_call_response.status_code == 401:
        token = oauth.get_new_token()
    else:
        print(api_call_response)

    return api_call_response.text
