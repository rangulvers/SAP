import flask
import os

app = flask.Flask(__name__)

cf_port = os.getenv("PORT")


# Only get method by default
@app.route('/')
def hello():
    return "Hello World"

# return JSON
@app.route('/json')
def return_json():
    return flask.jsonify(cf_port)


if __name__ == '__main__':
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=True)
