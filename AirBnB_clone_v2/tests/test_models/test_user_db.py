#!/usr/bin/python3
"""
Test the database version of User
"""
from os import environ
environ["HBNB_TYPE_STORAGE"] = "db"
from models import user
from models.base_model import BaseModel
from datetime import datetime
import unittest
User = user.User


class TestUser_db(unittest.TestCase):
    """Test the User class with db storage"""

    attributes = {'email': "johndoe@gmail.com",
                    'password': "j0hn",
                    'first_name': "John",
                    'last_name': "Doe"}

    row = User(**attributes)

    def test_mysql_obj(self):
        """Test that instance ORM object"""
        self.assertTrue(hasattr(self.row, '_sa_instance_state'))

    def test_table_name(self):
        """Test that table name is users"""
        self.assertEqual(self.row.__tablename__, "users")

    def test_time_obj(self):
        """Test that created_at and updated_at is date and time object"""
        self.assertTrue(type(self.row.created_at), datetime)
        self.assertTrue(type(self.row.updated_at), datetime)
        self.assertEqual(type(self.row), User)


    def test_isChild(self):
        """Test if instance is child of User"""
        self.assertIsInstance(self.row, User)

    def test_attributes(self):
        """Test for required attr for table users"""
        self.attributes.update({'id': None, 'reviews': None, 'places': None})
        for attr in self.attributes.keys():
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.row, attr))
