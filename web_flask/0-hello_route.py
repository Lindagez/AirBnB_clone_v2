#!/usr/bin/python3
# importing flask
'''
script that starts a Flask web application
'''
from flask import Flask


app = Flask(__name__)

# app decorator for routing


@app.route('/', strict_slashes=False)
def hello():
    '''
    simple route
    Returns:
        str : Hello HBNB!
    '''
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
