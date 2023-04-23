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
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    ''' run the app '''
    app.run(host='0.0.0.0', port=5000)
