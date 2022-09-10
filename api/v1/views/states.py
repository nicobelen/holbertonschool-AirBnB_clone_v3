#!/usr/bin/python3
"""New view for State objects that handles all default RESTFul API actions"""

from crypt import methods
from flask import Flask, jsonify
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'])
def allStates():
    """ Retrieves the list of all State objects """
    return

@app_views.route('/states/<state_id>', methods=['GET'])
def state():
    """ Retrieves a State object """
    return

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state():
    """ Deletes a State object """
    return