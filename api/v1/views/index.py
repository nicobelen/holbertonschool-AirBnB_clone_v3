#!/usr/bin/python3
""" This is the index file"""

from api.v1.views import app_views
<<<<<<< HEAD
from flask import jsonify
from models import storage
=======
from flask import jsonify, Flask
from models.engine import file_storage
>>>>>>> 8be8e3a6eee1692ee80ecfbd37aec5b6eec9314f


@app_views.route('/status')
def status():
    """returns a JSON: "status": \"OK\""""
    return (jsonify({"status": "OK"}))


@app_views.route('/api/v1/stats')
def stats():
    """retrieves the number of each objects by type"""
    storage.count()
