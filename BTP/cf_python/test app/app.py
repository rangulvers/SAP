from flask import Flask
import os

app = Flask(__name__)

cf_port = os.getenv("PORT")


# Only get method by default
@app.route('/')
def hello():
    return "Hello World"


if __name__ == '__main__':
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=True)
