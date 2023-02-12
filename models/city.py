#!/usr/bin/python3
""" This module defines the class `City` """
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents the location (City)
    Attributes:
        name (str): name of the City
        state_id (str): the id of the state
    """

    state_id = ""
    name = ""
