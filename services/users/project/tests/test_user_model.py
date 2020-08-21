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
        self.assertTrue(user.pasword)

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


if __name__ == '__main__':
    unittest.main()
