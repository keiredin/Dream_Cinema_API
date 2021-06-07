from db import db
from datetime import datetime
from enum import unique

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean, default=True)
    image = db.Column(db.String(100), default='user.png')
    twitter_link = db.Column(db.String(40))
    instagram_link = db.Column(db.String(40))


    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()