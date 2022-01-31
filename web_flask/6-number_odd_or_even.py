#!/usr/bin/python3
"""
    /number/<n>: display “n is a number”
    only if n is an integer
"""


from flask import Flask, render_template


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_n(n):
    """ display HTML """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def render_even_odd(n):
    """ display HTML """
    eo = 'odd'
    if n % 2 == 0:
        eo = 'even'
    return render_template('6-number_odd_or_even.html', num=n, evenodd=eo)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
