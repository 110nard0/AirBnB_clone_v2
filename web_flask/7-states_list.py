#!/usr/bin/python3
"""Starts a Flask web application that fetches data from storage engine
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states():
    """Displays a HTML page with a list of all states in current db session
    """
    states = storage.all('State')
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
