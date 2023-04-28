#!/usr/bin/python3
"""Starts a Flask web application that fetches data from storage engine
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb')
def states():
    """Displays a HTML page for the AirBnB clone page
    """
    states = storage.all('State')
    places = storage.all('Place')
    amenities = storage.all('Amenity')
    return render_template('100-hbnb.html', states=states,
                           places=places, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
