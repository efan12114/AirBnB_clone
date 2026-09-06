#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up test method."""
        self.user = User()

    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attribute_types(self):
        """Test that User attributes are strings and default to empty strings."""
        self.assertIsInstance(User.email, str)
        self.assertEqual(User.email, "")
        self.assertIsInstance(User.password, str)
        self.assertEqual(User.password, "")
        self.assertIsInstance(User.first_name, str)
        self.assertEqual(User.first_name, "")
        self.assertIsInstance(User.last_name, str)
        self.assertEqual(User.last_name, "")

    def test_instance_attributes(self):
        """Test that a user instance can store custom attribute values."""
        self.user.email = "test@example.com"
        self.user.password = "secure123"
        self.user.first_name = "Efan"
        self.user.last_name = "Addis"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "secure123")
        self.assertEqual(self.user.first_name, "Efan")
        self.assertEqual(self.user.last_name, "Addis")


if __name__ == "__main__":
    unittest.main()