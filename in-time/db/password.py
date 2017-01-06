from db.load_db import db
from utils import password_md5

StringField = db.StringField


class PasswordField(StringField):

    def __init__(self):
        super().__init__(max_length=32)

    def set_value(self, instance, value):
        self.validate_wrap(value)
        obj_value = instance._values[self._name]
        obj_value.value = password_md5(value)
        obj_value.dirty = True
        obj_value.set = True
        obj_value.from_db = False
        if self.on_update != 'ignore':
            obj_value.update_op = self.on_update
