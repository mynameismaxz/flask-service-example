# main app
from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    # receive image url (successful)
    # sent to model api
    # waiting for output
    # show output
    model_output = requests.get('http://localhost:8081/recognition')
    return model_output.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)