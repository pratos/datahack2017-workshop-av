from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world(username=None):
	return("Welcome minion! your sacrifice has been accepted!".format(username))


@app.route('/minion/<string:username>')
def offerings(username=None):
	return("Welcome {}, your sacrifice has been accepted by the Demo Gods!".format(username))


@app.route('/webdemo')
def webdemo():
	return render_template('<img src="https://i.imgur.com/iZcUNxH.gifv" />')

if __name__ == '__main__':
	app.run(port=5000)