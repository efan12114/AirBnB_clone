#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel."""
        self.assertIsInstance(City(), BaseModel)

    def test_attribute_types(self):
        """Test City attribute types and defaults."""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertEqual(city.state_id, "")
        self.assertIsInstance(city.name, str)
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()