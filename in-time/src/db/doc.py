from flask_mongoalchemy import MongoAlchemy
from application.flask_config import app

db = MongoAlchemy(app)
Document = db.Document
DocumentField = db.DocumentField


class Doc(Document):

    def to_json(self):
        _dict = self.__dict__['_values']
        json = {}
        for k in _dict:
            if isinstance(_dict[k].value, ObjectId):
                json[k] = str(_dict[k].value)
            elif isinstance(_dict[k].value, MyDoc):
                json[k] = _dict[k].value.to_json()
            elif type(_dict[k].value) is list:
                json[k] = [
                    item if not isinstance(_dict[k].value, MyDoc)
                    else item.to_json() for item in _dict[k].value
                ]
            else:
                json[k] = _dict[k].value
        return json


class DocField(DocumentField):

    def __init__(self):
        super().__init__(Doc)