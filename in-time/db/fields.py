from mongoalchemy.fields.base import SCALAR_MODIFIERS
from db.load_db import db
from utils import md5_hex

StringField = db.StringField
Field = db.Field
IntField = db.IntField


class Md5Field(StringField):

    def __init__(self):
        super().__init__(max_length=32)

    def set_value(self, instance, value):
        self.validate_wrap(value)
        obj_value = instance._values[self._name]
        obj_value.value = md5_hex(value)
        obj_value.dirty = True
        obj_value.set = True
        obj_value.from_db = False
        if self.on_update != 'ignore':
            obj_value.update_op = self.on_update


class StringEnumField(StringField):

    def __init__(self, enum_cls, **kwargs):
        super().__init__(**kwargs)
        self.enum_cls = enum_cls
        self.enum_value = None

    def set_value(self, instance, item):
        self.validate_wrap(item)
        obj_value = instance._values[self._name]
        obj_value.value = item.value
        obj_value.enum_value = item
        obj_value.dirty = True
        obj_value.set = True
        obj_value.from_db = False
        if self.on_update != 'ignore':
            obj_value.update_op = self.on_update

    def validate_wrap(self, item):
        if not isinstance(item, self.enum_cls):
            self._fail_validation_type(value, self.enum_cls)
        super().validate_wrap(item.value)
