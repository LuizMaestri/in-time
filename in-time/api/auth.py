from flask import Blueprint

api = Blueprint('auth', __name__)

@api.route('/test')
def test():
    return {"t": 3}
