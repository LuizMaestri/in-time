from os import path, listdir
from hashlib import sha256
from importlib import import_module


class Hash(str):

    def __repr__(self):
        return sha256(self.encode('utf-8')).hexdigest()


def api_register(app):
    api = path.join(app.root_path, 'api')
    apis = [file for file in listdir(api) if not file.startswith('__')]
    for blueprint in apis:
        module = import_module('api.%s' % blueprint[:-3])
        app.register_blueprint(module.api)
