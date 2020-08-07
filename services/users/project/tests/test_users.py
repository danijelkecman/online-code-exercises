# services/users/project/tests/test_users.py

import json
import unittest

from project.tests.base import BaseTestCase
from project import db
from project.api.models import User


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user

class TestUserService(BaseTestCase): 
    """Tests for the Users Service."""
    
    def test_users(self):
        """Ensure the /ping route behaves correctly.""" 
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode()) 
        self.assertEqual(response.status_code, 200) 
        self.assertIn('pong!', data['message']) 
        self.assertIn('success', data['status'])


    def test_add_user(self):
        """Ensure a new user can be added to the database"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'danijel',
                    'email': 'danijel@danijel.co'
                }),
                content_type='application/json',
                )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('danijel@danijel.co was added!', data['message'])
            self.assertIn('success', data['status'])

    def test_add_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have username key."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'email': 'danijel@danijel.co'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_duplicate_email(self):
        """Ensure error is thrown if the email address already exist."""
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'daniejl',
                    'email': 'danijel@danijel.co'
                }),
                content_type='application/json'
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'daniejl',
                    'email': 'danijel@danijel.co'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry. That email already exsists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user(self):
        """Ensure get single user behaves correctly."""
        user = add_user('danijel', 'danijel@danijel.co')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('danijel', data['data']['username'])
            self.assertIn('danijel@danijel.co', data['data']['email'])
            self.assertIn('success', data['status'])

    
    def test_single_user_no_id(self):
        """Ensure error is thrown if an id is not provided"""
        with self.client:
            response = self.client.get('/users/noid')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])
            

    def test_single_user_incorrect_id(self):
        """Ensure error is thrown if the id does not exist"""
        with self.client:
            response = self.client.get('/users/111')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])


    def test_all_users(self):
        """Ensure get all users behaves correctly"""
        add_user('danijel', 'danijel@danijel.co')
        add_user('danijel1', 'danijel1@danijel.co')

        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('danijel', data['data']['users'][0]['username'])
            self.assertIn('danijel@danijel.co', data['data']['users'][0]['email'])
            self.assertIn('danijel1', data['data']['users'][1]['username'])
            self.assertIn('danijel1@danijel.co', data['data']['users'][1]['email'])

if __name__ == '__main__': 
    unittest.main()
