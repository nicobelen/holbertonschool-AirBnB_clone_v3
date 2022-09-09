#!/usr/bin/python3
""" source code - api """

from flask import Flask
from flask import Blueprint
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
#app_views = Blueprint(, '')


@app.teardown_appcontext
def calls_storage_close():
    storage.close()


if __name__ == '__main__':

    from os import getenv
    
    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")

    app.run(debug=False) #activar para que el servidor actualice los cambios
    app.run(threaded=True)
    
    if host is None or port is None:
        host = '0.0.0.0'
        port = '5000'
    
    app.run(host=host, port=port)
