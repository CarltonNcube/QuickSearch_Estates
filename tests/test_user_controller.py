#!/usr/bin/python3

import pytest
from backend.controllers.user_controller import create_user, update_user, delete_user, get_user

# Test UserController
def test_create_user():
    # Test creating a user
    user_data = {'username': 'test_user', 'email': 'test@example.com'}
    user_id = create_user(user_data)
    assert user_id is not None

def test_update_user():
    # Test updating a user
    user_data = {'username': 'test_user', 'email': 'test@example.com'}
    user_id = create_user(user_data)
    updated_user_data = {'username': 'updated_user', 'email': 'updated@example.com'}
    result = update_user(user_id, updated_user_data)
    assert result is True

def test_delete_user():
    # Test deleting a user
    user_data = {'username': 'test_user', 'email': 'test@example.com'}
    user_id = create_user(user_data)
    result = delete_user(user_id)
    assert result is True

def test_get_user():
    # Test getting a user
    user_data = {'username': 'test_user', 'email': 'test@example.com'}
    user_id = create_user(user_data)
    user = get_user(user_id)
    assert user['username'] == 'test_user'
    assert user['email'] == 'test@example.com'

