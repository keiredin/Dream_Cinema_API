from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import uuid
from . import app,api,ma,db

# from security import authenticate, identity
from resources.user import *
from resources.movie import *
# from resources.comment import *
# from resources.item import Item, ItemList
# from resources.store import Store, StoreList

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['PROPAGATE_EXCEPTIONS'] = True
# app.secret_key = 'mebea'
# api = Api(app)
# db.init_app(app)

# ma = Marshmallow(app)

@app.before_first_request
def create_tables():
    db.create_all()



# jwt = JWT(app, authenticate, identity)


# api.add_resource(Store, '/api/v1/store/<string:name>')
# api.add_resource(StoreList, '/api/v1/stores')
# api.add_resource(Item, '/api/v1/item/<string:name>')
# api.add_resource(UsersComment, '/api/v1/comment/')
api.add_resource(UsersRegister, '/api/v1/register/')
api.add_resource(UserRegister, '/api/v1/register/<int:id>')
api.add_resource(MovieList, '/api/v1/movies')
# api.add_resource(Movie, '/api/v1/movie/<int:id>')

if __name__ == '__main__':
    
    app.run(port=5000, debug=True)




