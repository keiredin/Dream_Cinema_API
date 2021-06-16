from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from backend.models.user import *
from backend.resources.user import UsersRegister





def authenticate(username, password):
    user = UserModel.find_by_email(username)

    if user and safe_str_cmp(user.Password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)











