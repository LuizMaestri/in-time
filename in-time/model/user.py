from flask_mongoalchemy import BaseQuery
from mongoalchemy.document import Index
from db.password import PasswordField
from db.doc import Doc, db as field


class UserQuery(BaseQuery):

    def authenticate(self, user):
        return self.filter(
            self.type.username == user.name,
            self.type.password == user.password
        ) is not None


class User(Doc):
    query_class = UserQuery
    name = field.StringField(max_length=150)
    username = field.StringField(max_length=50)
    password = PasswordField()
    image = field.StringField(required=False)

    index_username = Index().ascending('username').unique(drop_dups=True)
