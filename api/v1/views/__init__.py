#!/usr/bin/python3
""" connector """

from api.v1.views.index import *
from flask import Blueprint, Flask

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1/")
