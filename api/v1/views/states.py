#!/usr/bin/python3
"""New view for State objects that handles all default RESTFul API actions"""


from os import abort
from flask import Flask, jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'])
def allStates():
    """ Retrieves the list of all State objects """
    st = []
    for state in storage.all('State').values():
        st.append(state.to_dict())
    return jsonify(st)

@app_views.route('/states/<state_id>', methods=['GET'])
def state(state_id):
    """ Retrieves a State object """
    st = storage.get(State, state_id)
    if (st is None):
        abort(404)
    else:
        return jsonify(st.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ Deletes a State object """
    st = storage.get(State, state_id)
    if (st is None):
        abort(404)
    storage.delete(st)
    storage.save()
    return jsonify({}), 200
