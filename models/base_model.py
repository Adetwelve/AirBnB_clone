#!/usr/bin/python3
import uuid
from datetime import datetime
import models
""" This module defines a class `BaseModel` """


class BaseModel():
    """ Defines all common attributes/method of the BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initializes a new instance of BaseModel

        Args:
            *args (any): unused
            **kwargs (dict): key & value pair of attributes
        """

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Defines a string representation of the instance """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute `updated_at`
            with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/value
            of `__dict__` of the instance
        """

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
