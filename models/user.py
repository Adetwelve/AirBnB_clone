#!/usr/bin/python3
""" This module defines the class `User` """
from models.base_model import BaseModel


class User(BaseModel):
    """ Creates a new User
    Attributes:
        email (str): user's email
        password (str): user's password
        first_name (str): first name of the user
        last_name (str): last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
