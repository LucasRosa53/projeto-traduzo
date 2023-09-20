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
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym")
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        languages = cls._collection.find()
        language_dicts = []
        for language in languages:
            language_dict = {
                "name": language["name"],
                "acronym": language["acronym"],
            }
            language_dicts.append(language_dict)

        return language_dicts
