from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        self.data = data

    # Req. 2
    def to_dict(self):
        return {
            "_id": self.data.get("_id"),
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym")
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        languages = LanguageModel.find()
        language_dicts = []
        for language in languages:
            todict = language.to_dict()
            language_dicts.append(todict)

        return language_dicts
