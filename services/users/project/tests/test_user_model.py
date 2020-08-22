# services/users/project/tests/test_user_model.py

import unittest

from sqlalchemy.exc import IntegrityError

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from project.tests.utils import add_user


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = add_user('danijel', 'danijel@danijel.com', 'password')
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'danijel')
        self.assertEqual(user.email, 'danijel@danijel.com')
        self.assertTrue(user.active)
        self.assertTrue(user.password)

    def test_add_user_duplicate_username(self):
        add_user('danijel', 'danijel@danijel.com', 'password')
        duplicate_user = User(username='danijel', email='danijel@danijel.com', password='password')
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_add_user_duplicate_email(self):
        add_user('danijel', 'danijel@danijel.com', 'password')
        duplicate_user = User(username='danijel', email='danijel@danijel.com', password='password')
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        user = add_user('danijel', 'danijel@danijel.com', 'password')
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_encode_auth_token(self):
        user = add_user('danijel', 'danijel@danijel.com', 'test')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertEqual(User.decode_auth_token(auth_token), user.id)


if __name__ == '__main__':
    unittest.main()
