from inspect import ismethod


class Document:

    __database__ = ''

    def __init__(self):
        self._id = None
        self.a = 1

    def response_json(self):
        props = {}
        for name in dir(self):
            if not name.startswith('__'):
                value = getattr(self, name)
                if not ismethod(value):
                    props[name] = value
        return props

    def json(self):
        props = self.response_json()
        del props['_id']
        return props
