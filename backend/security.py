from werkzeug.security import safe_str_cmp
from backend.models.user import UserModel


def authenticate(Email, Password):
    user = UserModel.find_by_email(Email)
    print(user)
    return user
    print(safe_str_cmp(user.Password, Password))
    print(user.password)

    if user and safe_str_cmp(user.Password, Password):
        return user


def identity(payload): # payload is the content of the JWT token
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)