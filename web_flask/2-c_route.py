#!/usr/bin/python3
# importing flask
""" Starts a Flash Web Application C is FUN"""
from flask import Flask
app = Flask(__name__)
# app decorator for routing

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000) 

