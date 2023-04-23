#!/usr/bin/python3
'''
starts a Flask web application
'''

# importing modules

from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    '''
    remove the current SQLAlchemy Session
    '''
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def stateById(id=None):
    '''
    Returns a state information
    '''
    states = list(storage.all(State).values())
    if id is None:
        return render_template(
            "9-states.html",
            display="multiple",
            states=states,
        )
    else:
        res = list(filter(lambda x: x.id == id, states))
        state = res[0] if len(res) > 0 else False
        return render_template("9-states.html", display="single", state=state)


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
