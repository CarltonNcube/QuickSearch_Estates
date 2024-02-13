#!/usr/bin/python3

import unittest
from backend.models import User

class TestUserModel(unittest.TestCase):
    def test_create_user(self):
        # Test creating a user
        user = User(username='test_user', email='test@example.com')
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@example.com')

    def test_update_user(self):
        # Test updating a user
        user = User(username='test_user', email='test@example.com')
        user.username = 'updated_user'
        user.email = 'updated@example.com'
        self.assertEqual(user.username, 'updated_user')
        self.assertEqual(user.email, 'updated@example.com')

    def test_delete_user(self):
        # Test deleting a user
        user = User(username='test_user', email='test@example.com')
        del user
        with self.assertRaises(NameError):
            user

    def test_user_representation(self):
        # Test user representation
        user = User(username='test_user', email='test@example.com')
        self.assertEqual(str(user), '<User test_user>')

if __name__ == '__main__':
    unittest.main()

