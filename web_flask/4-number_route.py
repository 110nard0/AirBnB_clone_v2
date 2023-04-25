#!/usr/bin/python3
"""Starts a Flask web application
"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def hello():
    """Displays default query string
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def show():
    """Displays customized query string
    """
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """Displays a text based on input URI
    """
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """Displays a text based on input URI with default query string present
    """
    return "Python {}".format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>')
def number(n):
    """Displays valid string if input URI is an integer
    """
    return "{} is a number".format(escape(n))


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
