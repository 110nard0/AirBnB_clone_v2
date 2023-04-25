#!/usr/bin/python3
"""Starts a Flask web application
"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def hello():
    """Returns query string
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def display():
    """Displays query string
    """
    return "HBNB"


@app.route('/c/<text>')
def route_c(text):
    """Displays a text based on input URI
    """
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route('/python/')
@app.route('/python/<text>')
def route_python(text='is cool'):
    """Displays a text based on input URI with default value present
    """
    return "Python {}".format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
