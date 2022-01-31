#!/usr/bin/python3
"""
    /number/<n>: display “n is a number”
    only if n is an integer
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ display text """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display text """
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ display value """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_magic(text='is cool'):
    """ display default value """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_integer(n):
    """ display n if is integer """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
