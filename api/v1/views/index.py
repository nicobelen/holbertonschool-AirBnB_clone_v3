#!/usr/bin/python3
""" index """

from itertools import count
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    return (jsonify({"status": "OK"}))

@app_views.route('/api/v1/stats')
def stats():
    count()