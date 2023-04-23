#!/usr/bin/python3
'''
    script that starts a Flask web application:
'''

from flask import Flask, render_template

# importing storage, state & Amenity

from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(self):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    ''' lists States and amenities '''
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())

    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities)


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
