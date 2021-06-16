from backend import app
from flask_restplus import Api, Resource, fields
from backend import api
from flask_jwt import JWT, jwt_required, current_identity
from backend.resources.user import *
from backend.resources.movie import *
from backend.resources.comment import *
from backend.security import authenticate, identity
from backend.models.user import *



@app.before_first_request
def create_tables():
    db.create_all()



jwt = JWT(app, authenticate, identity)

api.add_resource(UserComment, '/api/v1/comment/<int:id>')
api.add_resource(UsersComment, '/api/v1/comment/')
api.add_resource(UsersRegister, '/api/v1/register')
api.add_resource(UserRegister, '/api/v1/register/<int:id>')
api.add_resource(MovieList, '/api/v1/movies')
api.add_resource(Movie, '/api/v1/movie/<int:id>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)