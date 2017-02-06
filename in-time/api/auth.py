<<<<<<< HEAD
from flask import Blueprint

api = Blueprint('auth', __name__)

@api.route('/test')
def test():
    return {"t": 3}
=======
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
>>>>>>> 7f760fa3439ade2f55bd42b78eaf95901ca2a41b
