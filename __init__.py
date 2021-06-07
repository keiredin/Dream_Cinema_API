from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import uuid
from flask_marshmallow import Marshmallow

from flask_sqlalchemy import SQLAlchemy

    



# from resources.comment import *
# from resources.item import Item, ItemList
# from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'mebea'
api = Api(app)
db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow(app)