#!/usr/bin/python3
"""Defines unittests for models/review.py."""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_is_subclass(self):
        """Test that Review is a subclass of BaseModel."""
        self.assertIsInstance(Review(), BaseModel)

    def test_attribute_types(self):
        """Test Review attribute types and defaults."""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)


if __name__ == "__main__":
    unittest.main()