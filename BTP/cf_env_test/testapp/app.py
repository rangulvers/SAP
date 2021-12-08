import flask
import os
import cfenv

app = flask.Flask(__name__)
cf_port = os.getenv("PORT")

testvar = os.getenv("TESTVAR")
# env = cfenv.AppEnv()
# api_service = env.get_service(label="destination")
# api_service.credentials


@app.route('/')
def home():
    """Landing Page"""
    return flask.render_template(
        'home.html',
        app_port=cf_port,
        page_title='Test Page ENV Test',
        api_url=testvar
    )


if __name__ == '__main__':
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=False)
