#!/usr/bin/python3
'''
    script that starts a Flask web application:
'''

from flask import Flask, render_template

# importing storage and state

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(self):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def listStates():
    ''' lists States '''
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def citiesByStates():
    ''' lists cities by states '''
    states = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
