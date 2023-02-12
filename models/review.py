#!/usr/bin/python3
""" This module defines the Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review
    Attributes:
        place_id (str): The Place id
        user_id (str): The User id
        text (str): The review
    """

    place_id = ""
    user_id = ""
    text = ""
