#!/usr/bin/python3
"""Start a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes = False)
def hello_hbnb():
    """Return query string
    """
    return "Hello, HBNB!"


if __name__ == "__main__":
#   app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
