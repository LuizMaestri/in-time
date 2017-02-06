from db.connection import Connection
from server import APP


HOST, PORT = APP.config['MONGO_HOST'], APP.config['MONGO_PORT']
DATABASE = APP.config['MONGO_DATABASE']

CONNECTION = Connection(database=DATABASE, host=HOST, port=PORT)
