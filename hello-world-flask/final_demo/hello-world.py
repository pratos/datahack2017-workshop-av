from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world(username=None):
	return("Welcome minion! your sacrifice has been accepted!".format(username))


@app.route('/minion/<string:username>')
def offerings(username=None):
	return("Welcome {}, your sacrifice has been accepted by the Demo Gods!".format(username))


@app.route('')

if __name__ == '__main__':
	app.run(port=5000)