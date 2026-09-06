#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel."""
        self.assertIsInstance(Amenity(), BaseModel)

    def test_attribute_types(self):
        """Test Amenity attribute types and defaults."""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()