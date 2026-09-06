#!/usr/bin/python3
"""Defines the BaseModel class for all other entities."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class defining all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        time_fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.strptime(value, time_fmt))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update updated_at with current datetime and trigger storage save."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance."""
        res_dict = self.__dict__.copy()
        res_dict["__class__"] = self.__class__.__name__
        res_dict["created_at"] = self.created_at.isoformat()
        res_dict["updated_at"] = self.updated_at.isoformat()
        return res_dict