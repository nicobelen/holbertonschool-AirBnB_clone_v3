#!/usr/bin/python3
"""New view for State objects that handles all default RESTFul API actions"""


from os import abort
from flask import Flask, jsonify, abort, request
from models import storage
from models.city import City
from api.v1.views import app_views

app_views.strict_slashes = False


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def all_cities(states_id):
    """ Retrieves the list of all State objects """

    st = []

    for city in storage.all('City').values():
        st.append(city.to_dict())

    return jsonify(st)


@app_views.route('/states/<state_id>', methods=['GET'])
def state(state_id):
    """ Retrieves a State object """

    st = storage.get(City, state_id)

    if (st is None):
        abort(404)
    else:
        return jsonify(st.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ Deletes a State object """

    st = storage.get(City, state_id)

    if (st is None):
        abort(404)

    storage.delete(st)
    storage.save()

    return jsonify({}), 200


@app_views.route('/states', methods=['POST'])
def create_state():
    """ Creates a State """

    dic = request.get_json()

    if (dic is None):
        abort(400, "Not a JSON")

    key = 'name'

    if dic[key] is None:
        abort(400, "Missing name")

    new_state = City(name=dic['name'])

    storage.save()
    return jsonify({new_state.to_dict}), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """ Updates a State object """

    storag = storage.get(City, state_id)

    if (storag is None):
        abort(404)

    dic = request.get_json()

    if (dic is None):
        abort(400, "Not a JSON")

    attributes = ['id', 'created_at', 'updated_at']

    for key, value in dic.items():
        if key not in attributes:
            setattr(storag, key, value)

    storag.save()

    return jsonify({storag.to_dict}), 200
