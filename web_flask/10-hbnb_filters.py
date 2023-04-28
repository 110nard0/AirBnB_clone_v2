#!/usr/bin/python3
"""Starts a Flask web application that fetches data from storage engine
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters')
def states():
    """Displays a HTML page with a list of filters for the AirBnB clone page
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
