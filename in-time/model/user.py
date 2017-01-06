from mongoalchemy.document import Index
from db.password import PasswordField
from db.doc import Doc, db as field


class User(Doc):
        name = field.StringField(max_length=150)
        username = field.StringField(max_length=50)
        password = PasswordField()
        image = field.StringField(required=False)

        index_username = Index().ascending('username').unique(drop_dups=True)
