#!/usr/bin/env python3

from flask import Blueprint, jsonify, request
from backend.controllers.user_controller import (delete_user, test, update_user, 
                                                  get_user_listings, get_user,
                                                  create_user, reset_password)
from utils.verify_user import verify_token

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/test', methods=['GET'])
def test_route():
    return test()

@user_routes.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    return create_user(data)

@user_routes.route('/update/<int:id>', methods=['POST'])
@verify_token
def update(id):
    data = request.get_json()
    return update_user(id, data)

@user_routes.route('/delete/<int:id>', methods=['DELETE'])
@verify_token
def delete(id):
    return delete_user(id)

@user_routes.route('/listings/<int:id>', methods=['GET'])
@verify_token
def listings(id):
    return get_user_listings(id)

@user_routes.route('/<int:id>', methods=['GET'])
@verify_token
def get(id):
    return get_user(id)

@user_routes.route('/reset-password/<int:id>', methods=['POST'])
@verify_token
def reset_password_route(id):
    data = request.get_json()
    return reset_password(id, data)

# Export the Blueprint
user_routes_blueprint = user_routes

