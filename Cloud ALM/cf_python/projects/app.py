import flask
import os
import modules.calm as calm
import modules.oauth as oauth
import json
import cfenv

app = flask.Flask(__name__)

cf_port = os.getenv("PORT")

env = cfenv.AppEnv()


@app.route('/')
def home():
    """Landing Page"""
    return flask.render_template(
        'home.html',
        app_port=cf_port,
        page_title='Test Page'
    )


@app.route('/projects')
def getProjects():

    token = oauth.get_new_token(auth_server_url, client_id, client_secret)
    calmprojects = calm.get_projects(token)
    """Get all Projects"""
    # return calmprojects
    return flask.render_template(
        'projects.html',
        projects=json.loads(calmprojects)
    )


@app.route('/tasks')
def getTasks():

    token = oauth.get_new_token(auth_server_url, client_id, client_secret)
    projectid = flask.request.args.get('project')
    calm_tasks = calm.get_tasks(
        token, projectid)
    """Get all Projects"""
    # return calm_tasks
    return flask.render_template(
        'tasks.html',
        projectid=projectid,
        tasks=json.loads(calm_tasks)
    )


if __name__ == '__main__':
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=False)
