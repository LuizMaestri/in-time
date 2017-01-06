from db.doc import Doc, db as field
from db.password import PasswordField


class User(Doc):
        name = field.StringField(max_length=150)
        password = PasswordField()
