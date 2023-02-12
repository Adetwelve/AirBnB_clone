#!/usr/bin/python3
""" This module defines the class `Amenity` """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Represents an amenity in the AirBnB
    Attributes:
        name (str): name of the amenity
    """

    name = ""
