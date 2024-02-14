#!/usr/bin/python3

import pytest
from backend.models import User

# Test User Model
def test_create_user():
    # Test creating a user
    user = User(username='test_user', email='test@example.com')
    assert user.username == 'test_user'
    assert user.email == 'test@example.com'

def test_update_user():
    # Test updating a user
    user = User(username='test_user', email='test@example.com')
    user.username = 'updated_user'
    user.email = 'updated@example.com'
    assert user.username == 'updated_user'
    assert user.email == 'updated@example.com'

def test_delete_user():
    # Test deleting a user
    user = User(username='test_user', email='test@example.com')
    del user
    with pytest.raises(NameError):
        user

def test_user_representation():
    # Test user representation
    user = User(username='test_user', email='test@example.com')
    assert str(user) == '<User test_user>'

