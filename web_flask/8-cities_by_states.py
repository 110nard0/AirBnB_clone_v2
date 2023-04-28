#!/usr/bin/python3
"""Starts a Flask web application that fetches data from storage engine
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def cities():
    """Displays a HTML page with a list of all cities in every state
    """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
