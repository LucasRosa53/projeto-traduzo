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
            "name": self.data.get("name", ""),
            "acronym": self.data.get("acronym", "")
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        languages = cls.find()
        languages_dicts = [language.to_dict() for language in languages]
        return languages_dicts
