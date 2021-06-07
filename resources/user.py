from flask_restplus import Resource, reqparse
from models.user import UserModel
from flask_jwt import *



class UsersRegister(Resource):
    # @jwt_required
    def get(self):
        users = UserModel.query.all()
        return {"Users" : list(map(lambda u:u.jsonify(), users))}

    

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    

    def post(self):
        data = UsersRegister.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "A user with that email  already exists"}, 400

        user = UserModel(data['username'], data['password'], data['email'])
        user.save_to_db()
        

        return {"message": "User created successfully."}, 201

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    


    def get(self, id):
        user = UserModel.find_by_id(id)
        if user:
            return {f"User {user.id}" : user.jsonify()}, 200
        return {"message": "User is not found!"}, 404

    
    def put(self, id):
        # users = UserModel.query.all()
        user = UserModel.find_by_id(id)
        data = request.get_json()
        
        if user:
        #     if UserModel.find_by_email(data['email']):
        #         return {"message":"This email already taken"}
        #     else:
            # for key in data.keys():
            #     user.key = data[key]
            #     user.save_to_db()
            return data.keys()., 200
        return {"message": "User is not found!"}, 404

        # users = UserModel.query.all()
        # user = UserModel.find_by_id(id)
        # data = UserRegister.parser.parse_args()
        # if user:
        #     if UserModel.find_by_email(data['email']):
        #         return {"message":"This email already taken"}
        #     else:
        #         user.username = data['username']
        #         user.email = data['email']
        #         user.password = data['password']
        #         user.save_to_db()
        #         return {"message": "User updated!"}, 200
        # return {"message": "User is not found!"}, 404

    def delete(self, id):
        user = UserModel.find_by_id(id)
        if user:
            user.delete_from_db()
            return {"message": "User is successfully deleted!"}, 200
        return {"message": "User is not found!"}, 404
    # # def get(self, name):
    # #     user = UserModel.find_by_email(name)
    # #     return user
    # #     return {f"User {user.id}" : user.jsonify()}