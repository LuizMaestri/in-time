from pymongo import MongoClient


class __Connection(type):
    def __getitem__(cls, key):
        return cls.__connections__[key]



class Connection(object, metaclass=__Connection):

    __connections__ = {}


    def __new__(cls, database, host='localhost', port=27017):
        if not cls.__connections__.get(database, None):
            cls.__connections__[database] = MongoClient(host, port)
        return super().__new__(cls)
