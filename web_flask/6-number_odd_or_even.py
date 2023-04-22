#!/usr/bin/python3
""" Starts a Flash Web Application from flask import Flask, render_template"""
from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/', strict_slashes=False)
def hello_hbnb():
     """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
     """Displays  HBNB!'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
 """Displays 'C ', followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """Displays 'Python '"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
 """Displays 'n is a number' if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
        """Displays a HTML page with 'Number: n' """
    return render_template('5-number.html', value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
        """Displays a HTML page with 'Number: n is even|odd' """
    return render_template('6-number_odd_or_even.html', value=n)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

