#!/usr/bin/python3

import unittest
from backend.controllers.user_controller import create_user, update_user, delete_user, get_user

class TestUserController(unittest.TestCase):
    def test_create_user(self):
        # Test creating a user
        user_data = {'username': 'test_user', 'email': 'test@example.com'}
        user_id = create_user(user_data)
        self.assertIsNotNone(user_id)

    def test_update_user(self):
        # Test updating a user
        user_data = {'username': 'test_user', 'email': 'test@example.com'}
        user_id = create_user(user_data)
        updated_user_data = {'username': 'updated_user', 'email': 'updated@example.com'}
        result = update_user(user_id, updated_user_data)
        self.assertTrue(result)

    def test_delete_user(self):
        # Test deleting a user
        user_data = {'username': 'test_user', 'email': 'test@example.com'}
        user_id = create_user(user_data)
        result = delete_user(user_id)
        self.assertTrue(result)

    def test_get_user(self):
        # Test getting a user
        user_data = {'username': 'test_user', 'email': 'test@example.com'}
        user_id = create_user(user_data)
        user = get_user(user_id)
        self.assertEqual(user['username'], 'test_user')
        self.assertEqual(user['email'], 'test@example.com')

if __name__ == '__main__':
    unittest.main()

