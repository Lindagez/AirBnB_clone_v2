#!/usr/bin/python3
""" from flask import Flask, escape, request, render_template"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
    
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n,int):
    return render_template('5-number.html', value=n)
    else:
        return"notfound",404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

