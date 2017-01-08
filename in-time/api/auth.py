from application.flask_config import app
from model.user import User
from flask import request


@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    user = User(**request.data)
    return {
        'authenticate': User.query.authenticate(user),
        'user': user.to_json()
    }
