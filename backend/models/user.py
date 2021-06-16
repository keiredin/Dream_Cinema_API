from datetime import datetime
from enum import unique
from backend import db
from backend import app

app.app_context().push()

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(30), nullable=False, unique=True)
    Password = db.Column(db.String(100), nullable=False)
    Admin = db.Column(db.Boolean, default=False)
    Image = db.Column(db.String(100), default='user.png')
    Twitter_link = db.Column(db.String(40))
    Instagram_link = db.Column(db.String(40))


    # def __init__(self, username, password, email):
    #     print(UserModel.query.all())
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(Email=email).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(Username=username).first()

    

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    
    # def jsonify(self):
    #     return {
    #         "username" : self.username,
    #         "email" : self.email,
    #         "admin" : self.admin
    #     }