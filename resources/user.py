from flask import request
from flask_restplus import Resource, reqparse, Api, fields
from flask_jwt import *
from Dream_Cinema_API.models.user import *
from Dream_Cinema_API.ma import *
from Dream_Cinema_API import api



user_schema = UserSchema()
users_schema = UserSchema(many=True)



class UsersRegister(Resource):
    # @jwt_required

    # Model required by flask_restplus for expect
    user = api.model("User", {
        'Username': fields.String('Name of the user'),
        'Email': fields.String,
        'Password': fields.String
        
    })

    
    def get(self):
        users = UserModel.query.all()
        return users_schema.dump(users)
        # return {"Users" : list(map(lambda u:u.jsonify(), users))}

    @api.expect(user)
    def post(self):
        new_user = UserModel()
        new_user.Username = request.json['Username']
        new_user.Email = request.json['Email']
        new_user.Password = request.json['Password']

        new_user.save_to_db()
        return user_schema.dump(new_user)
        # data = UsersRegister.parser.parse_args()

        # if UserModel.find_by_email(data['email']):
        #     return {"message": "A user with that email  already exists"}, 400

        # user = UserModel(data['username'], data['password'], data['email'])
        # user.save_to_db()

    # parser = reqparse.RequestParser()
    # parser.add_argument('username',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('password',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('email',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )

    

    # def post(self):
    #     user = UserModel
    #     new_dinner.Title = request.json['Title']
    #     new_dinner.EventDate = request.json['EventDate']
    #     new_dinner.Description = request.json['Description']
    #     # data = UsersRegister.parser.parse_args()

    #     # if UserModel.find_by_email(data['email']):
    #     #     return {"message": "A user with that email  already exists"}, 400

    #     # user = UserModel(data['username'], data['password'], data['email'])
    #     # user.save_to_db()
        

#         # return {"message": "User created successfully."}, 201

class UserRegister(Resource):

    def get(self, id):
        user = UserModel.find_by_id(id)
        if user:
            return user_schema.dump(user),200
        return {"message": "User is not found!"}, 404


    def put(self, id):
        # users = UserModel.query.all()
        user = UserModel.find_by_id(id)
        data = request.json()
        
        if user:
            if UserModel.find_by_email(data['email']):
                return {"message":"This email already taken"}
            else:
                for key in data.keys():
                    user.key = data[key]
                    user.save_to_db()
                return data.keys(), 200
        return {"message": "User is not found!"}, 404

        users = UserModel.query.all()
        user = UserModel.find_by_id(id)
        data = UserRegister.parser.parse_args()
        if user:
            if UserModel.find_by_email(data['email']):
                return {"message":"This email already taken"}
            else:
                user.username = data['username']
                user.email = data['email']
                user.password = data['password']
                user.save_to_db()
                return {"message": "User updated!"}, 200
        return {"message": "User is not found!"}, 404
    

    def delete(self, id):
        user = UserModel.find_by_id(id)
        if user:
            user.delete_from_db()
            return {"message": "User is successfully deleted!"}, 200
        return {"message": "User is not found!"}, 404
#     parser = reqparse.RequestParser()
#     parser.add_argument('username',
#                         type=str,
#                         required=True,
#                         help="This field cannot be blank."
#                         )
#     parser.add_argument('password',
#                         type=str,
#                         required=True,
#                         help="This field cannot be blank."
#                         )
#     parser.add_argument('email',
#                         type=str,
#                         required=True,
#                         help="This field cannot be blank."
#                         )
    


#     def get(self, id):
#         user = UserModel.find_by_id(id)
#         if user:
#             return {f"User {user.id}" : user.jsonify()}, 200
#         return {"message": "User is not found!"}, 404

    
#     def put(self, id):
#         # users = UserModel.query.all()
#         user = UserModel.find_by_id(id)
#         data = request.get_json()
        
#         # if user:
#         # #     if UserModel.find_by_email(data['email']):
#         # #         return {"message":"This email already taken"}
#         # #     else:
#         #     # for key in data.keys():
#         #     #     user.key = data[key]
#         #     #     user.save_to_db()
#         #     return data.keys(), 200
#         return {"message": "User is not found!"}, 404

#         # users = UserModel.query.all()
#         # user = UserModel.find_by_id(id)
#         # data = UserRegister.parser.parse_args()
#         # if user:
#         #     if UserModel.find_by_email(data['email']):
#         #         return {"message":"This email already taken"}
#         #     else:
#         #         user.username = data['username']
#         #         user.email = data['email']
#         #         user.password = data['password']
#         #         user.save_to_db()
#         #         return {"message": "User updated!"}, 200
#         # return {"message": "User is not found!"}, 404

    
    # # def get(self, name):
    # #     user = UserModel.find_by_email(name)
    # #     return user
    # #     return {f"User {user.id}" : user.jsonify()}