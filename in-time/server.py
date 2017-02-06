from application.flask_json import FlaskJSON
from importlib import import_module
from utils import api_register
from os import path, environ
from db.doc import Document

APP = FlaskJSON(__name__)
CONFIG_FILE = path.join(APP.root_path, 'config.cfg')
APP.config.from_pyfile(CONFIG_FILE, silent=True)

api_register(APP)

Dao = import_module('db.dao').Dao
