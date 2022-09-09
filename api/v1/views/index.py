#!/usr/bin/python3
""" index """

from api.v1.views import app_views
from flask import jsonify
from models.engine import file_storage


@app_views.route('/status')
def status():
    """returns a JSON: "status": \"OK\""""
    return (jsonify({"status": "OK"}))


@app_views.route('/api/v1/stats')
def stats():
    """retrieves the number of each objects by type"""
    file_storage.count()
