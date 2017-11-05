import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify("Hello World")


@app.route('/minion/<string:username>')
def another_function(username=None):
    return("Welcome {}".format(username))

if __name__ == '__main__':
    app.run(port=5000)
