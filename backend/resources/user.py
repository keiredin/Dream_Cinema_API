from flask import request,jsonify
from flask_restplus import Resource, reqparse, Api, fields
from flask_jwt import *
from flask_jwt import jwt_required
import json

from backend.models.user import *
from backend.ma import *
from backend import api


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Model required by flask_restplus for expect
user = api.model("User", {
    'Username': fields.String('Name of the user'),
    'Email': fields.String,
    'Password': fields.String
    
})
class UsersRegister(Resource):
    # @jwt_required
    def get(self):
        ''' 
            Get All Users from the Database
        '''
        users = UserModel.query.all()
        return users_schema.dump(users),200 if users else 404
    

    @api.expect(user)
    def post(self):
        '''
            Create a new User
        '''
        Username = request.json['Username']
        Email = request.json['Email']
        Password = request.json['Password']

        if UserModel.find_by_email(Email):
            return {"message": "Email is already taken"}, 409
        
        new_user = UserModel()
        new_user.Username = Username
        new_user.Email = Email
        new_user.Password = Password
        new_user.save_to_db()
        return user_schema.dump(new_user), 201
        

class UserRegister(Resource):
    
    def get(self, id):
        '''
            Get a User by id
        '''
        user = UserModel.find_by_id(id)
        if user:
            return user_schema.dump(user),200
        return {"message": "User is not found!"}, 404

    
    @api.expect(user)
    def put(self, id):
        '''
            Update an existing User
        '''
        # user = UserModel.find_by_id(id)
        # userd = user_schema.dump(user)
        # data = request.get_json()
        # j = []
        # for i in data:
        #     j.append(i)
        
        # for item in j:
        #     if item == userd[item]


        # users = UserModel.query.all()
        user = UserModel.find_by_id(id)
        
        new_username = request.json['Username']
        new_email = request.json['Email']
        new_password = request.json['Password']

        # for key in data.

        
        
        if user:
            if UserModel.find_by_email(new_email):
                return {"message":"This email already taken"},100
            else:
                user.Username = new_username
                user.Email = new_email
                user.Password = new_password
                user.save_to_db()
                
                return user_schema.dump(user), 200

        return {"message": "User is not found!"}, 404

        
    
    @jwt_required()
    def delete(self, id):
        '''
            delete a user from database
        '''
        user = UserModel.find_by_id(id)
        if user:
            user.delete_from_db()
            return {"message": "User is successfully deleted!"}, 200
        return {"message": "User is not found!"}, 404

