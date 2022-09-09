#!/usr/bin/python3
""" connector """

from api.v1.views.index import *
from flask import Blueprint

app_views = Blueprint(url_prefix="/api/v1/")
