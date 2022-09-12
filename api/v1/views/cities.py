#!/usr/bin/python3
"""New view for State objects that handles all default RESTFul API actions"""


from os import abort
from flask import Flask, jsonify, abort, request
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views

app_views.strict_slashes = False


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def all_cities(state_id):
    """ Retrieves the list of all City objects linked to state_id"""
    ct = storage.get(State, state_id)
    cities_list = []

    if (ct is None):
        abort(404)
    else:
        city = storage.all('City')
        for ob in city.values():
            if (ob.todict()['state_id'] == state_id):
                cities_list.append(ob.to_dict())
    return jsonify(cities_list)


@app_views.route('/cities/<city_id>', methods=['GET'])
def city(city_id):
    """ Retrieves a City object """
    ct = storage.get(City, city_id)

    if (ct is None):
        abort(404)
    else:
        return jsonify(ct.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """ Deletes a City object """

    ct = storage.get(City, city_id)

    if (ct is None):
        abort(404)

    storage.delete(ct)
    storage.save()

    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """ Creates a State """
    st = storage.get(State, state_id)
    dic = request.get_json()

    if (st is None):
        abort(404)

    if (dic is None):
        abort(400, "Not a JSON")

    key = 'name'

    if dic[key] is None:
        abort(400, "Missing name")

    dic['state_id'] == state_id
    new_city = City(**dic)
    storage.new(new_city)
    storage.save()
    return jsonify({dic.to_dict}), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """ Updates a State object """

    ct = storage.get(City, city_id)

    if (ct is None):
        abort(404)

    dic = request.get_json()

    if (dic is None):
        abort(400, "Not a JSON")

    attributes = ['id', 'state_id', 'created_at', 'updated_at']

    for key, value in dic.items():
        if key not in attributes:
            setattr(ct, key, value)

    ct.save()
    storage.save()

    return jsonify({ct.to_dict}), 200
