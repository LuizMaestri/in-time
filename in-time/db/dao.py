from db.db_config import APP, CONNECTION, Connection
from db.doc import Document


class Dao:

    __dao__ = None

    def __new__(cls):
        if not cls.__dao__:
            cls.__dao__ = super().__new__(cls)
        return cls.__dao__

    def __init__(self):
        self.database = APP.config['MONGO_DATABASE']

    def save(self, doc: Document):
        client = Connection[self.database]
        database = client[self.database]
        collection = database[type(doc).__name__]
        json = doc.json()
        result = collection.update_one({
            '_id': doc._id
        }, {
            '$set': json
        })
        if result.matched_count == 0 and result.modified_count == 0:
            result = collection.insert_one(json)
            doc._id = result.inserted_id
        return doc 
