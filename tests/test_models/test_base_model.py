#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up test methods."""
        self.bm = BaseModel()

    def tearDown(self):
        """Clean up after test methods."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """Test proper initialization and attribute types."""
        self.assertIsInstance(self.bm, BaseModel)
        self.assertTrue(hasattr(self.bm, "id"))
        self.assertTrue(hasattr(self.bm, "created_at"))
        self.assertTrue(hasattr(self.bm, "updated_at"))
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str(self):
        """Test the string representation of BaseModel."""
        str_repr = str(self.bm)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn(self.bm.id, str_repr)
        self.assertIn("r", str_repr)

    def test_save(self):
        """Test that save() updates the updated_at timestamp and writes to file."""
        old_updated = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(old_updated, self.bm.updated_at)
        self.assertTrue(os.path.exists("file.json"))

    def test_to_dict(self):
        """Test to_dict() returns a dictionary with proper format and keys."""
        bm_dict = self.bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertIsInstance(bm_dict["created_at"], str)
        self.assertIsInstance(bm_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()