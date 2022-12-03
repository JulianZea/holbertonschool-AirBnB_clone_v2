#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
from flask import render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """This function returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """This fuction displays  “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ display number int """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def func_odd_even(n):
    """ Only enter the module if n is an odd or even number """
    oddEven = "even" if (n % 2 == 0) else "odd"
    return render_template("6-number_odd_or_even.html", n=n, oddEven=oddEven)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
