import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/donate')
def donate():
    return flask.render_template('donate.html')

@app.route('/history')
def history():
    return flask.render_template('history.html')

app.run(
    port = int(os.getenv('PORT',8086)),
    host = os.getenv('IP', '127.0.0.1')
)