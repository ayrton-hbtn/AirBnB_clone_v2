#!/usr/bin/python3
"""
    /python/(<text>): display “Python ”, followed by the value
    of the text variable (replace underscore _ symbols with a space)
    The default value of text is “is cool”
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
