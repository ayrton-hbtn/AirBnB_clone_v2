#!/usr/bin/python3
""" App Flask """

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    """ Display the states"""
    storage_states = storage.all('State')
    return render_template('7-states_list.html', storage_states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_cities(id):
    """ Display cities by id State """
    storage_states = storage.all('State')
    id_state = '{}.{}'.format('State', id)
    if is_state in storage_states:
        storage_states = storage_states[id_state]
    else:
        storage_states = None
    return render_template('9-states.html', storage_states=states)


@app.teardown_appcontext
def teardown(self):
    """ close storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
