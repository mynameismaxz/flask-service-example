#model app
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/recognition')
def recognition():
    # receive url of image
    # download
    # convert to numpy
    # compare with model
    # result -> pack to json
    # sent to client (bla bla bla...)
    return jsonify(
        response=200,
        result="แกงเขียวหวาน",
        prob=0.99
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)