#!/usr/bin/python3
""" source code - API """

from os import getenv
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def calls_storage_close(self):
    """ closes the storage """
    storage.close()


@app.errorhandler(404)
def error_404(error):
    """ error status for paths not found """
    msg_error = {"error": "Not found"}
    return jsonify(msg_error), 404


if __name__ == '__main__':

    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
