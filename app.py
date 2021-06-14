from Dream_Cinema_API import app
from flask_restplus import Api, Resource, fields
from Dream_Cinema_API import api
  
from Dream_Cinema_API.resources.user import *
from Dream_Cinema_API.resources.movie import *



@app.before_first_request
def create_tables():
    db.create_all()





# jwt = JWT(app, authenticate, identity)
# api.add_resource(Store, '/api/v1/store/<string:name>')
# api.add_resource(StoreList, '/api/v1/stores')
# api.add_resource(Item, '/api/v1/item/<string:name>')
# api.add_resource(UsersComment, '/api/v1/comment/')
api.add_resource(UsersRegister, '/api/v1/register')
api.add_resource(UserRegister, '/api/v1/register/<int:id>')
# api.add_resource(MovieList, '/api/v1/movies')
# api.add_resource(Movie, '/api/v1/movie/<int:id>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)