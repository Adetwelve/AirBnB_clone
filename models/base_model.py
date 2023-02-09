#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_2 = self.__dict__.copy()
        dict_2["__class__"] = self.__class__.__name__
        dict_2["created_at"] = self.created_at.isoformat()
        dict_2["updated_at"] = self.updated_at.isoformat()
        return dict_2
