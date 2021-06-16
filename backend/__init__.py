
from flask import Flask
from flask_restplus import Api, Resource, fields
from flask_jwt import JWT
import uuid
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'dreamcinema123fdjkernfj12nkjwfnejwfknnjvndiufv'




db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow(app)

api = Api(app,version='1.0',title='Dream Cinema API',
          description='A simple Cinema API')


