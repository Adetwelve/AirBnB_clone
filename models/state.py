#!/usr/bin/python3
""" This module defines the class `State` """
from models.base_model import BaseModel


class State(BaseModel):
    """ Represents the location (State)
    Attributes:
        name (str): name of the State
    """

    name = ""
