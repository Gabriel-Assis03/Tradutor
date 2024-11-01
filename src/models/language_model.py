from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        self.data = data.copy()

    # Req. 2
    def to_dict(self):
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"]
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        ret = []
        data = cls._collection.find()
        for lang in data:
            ret.append({
                "name": lang["name"],
                "acronym": lang["acronym"]
            })
        return ret
