#!/usr/bin/python3
""" source code - api """

from api.v1.views import app_views
from flask import Blueprint
from flask import Flask
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def calls_storage_close(self):
    """ closes the storage """
    storage.close()


if __name__ == '__main__':

    from os import getenv

    host = getenv("HBNB_API_HOST", '0.0.0.0')
    port = getenv("HBNB_API_PORT", '5000')

    app.run(debug=False)  # activar para que el servidor actualice los cambios
    app.run(threaded=True)

    app.run(host=host, port=port)
