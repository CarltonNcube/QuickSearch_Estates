#!/usr/bin/python3

from flask import Blueprint

# Initialize a Blueprint object for user routes
user_routes = Blueprint("user_routes", __name__)

# Initialize a Blueprint object for property routes
property_routes = Blueprint("property_routes", __name__)

# Import routes for user and property
from . import user_routes
from . import property_routes
