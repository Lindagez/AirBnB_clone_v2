#!/usr/bin/python3
# importing flask
'''
script that starts a Flask web application
'''
from flask import Flask, escape, render_template

app = Flask(__name__)

# app decorator for routing


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    new_txt = text.replace('_', ' ')
    return 'C %s' % escape(new_txt)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_lang(text='is cool'):

    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_no(n):
    return render_template('5-number.html', no=n)


if __name__ == '__main__':
    ''' run the app '''
    app.run(host='0.0.0.0', port=5000)
