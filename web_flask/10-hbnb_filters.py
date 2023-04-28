#!/usr/bin/python3
"""Starts a Flask web application that fetches data from storage engine
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """Displays a HTML page with a list of all states by id
    """
    states = storage.all('State')
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
