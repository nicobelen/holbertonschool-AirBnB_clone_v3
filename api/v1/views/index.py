#!/usr/bin/python3
""" This is the index file"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


classes = {"Amenity": storage.count('Amenity'), "BaseModel": storage.count('BaseModel'), "City": storage.count('City'),
           "Place": storage.count('Place'), "Review": storage.count('Review'), "State": storage.count('State'), "User": storage.count('User')}


@app_views.route('/status')
def status():
    """returns a JSON: "status": \"OK\""""
    return (jsonify({"status": "OK"}))


@app_views.route('/stats')
def stats():
    """retrieves the number of each objects by type"""
    class_dir = {}
    for key in classes.items():
        class_dir.update(key)
    return jsonify(class_dir)
