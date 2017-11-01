import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
	return("Hello, World")


# @app.route('/minion/<string:username>')
# def offerings(username=None):
# 	return("Welcome {}".format(username))


if __name__ == '__main__':
	app.run(port=5000)