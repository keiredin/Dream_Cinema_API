from flask_restplus import Resource, reqparse
from models.comment import CommentModel
from datetime import datetime
from flask_jwt import *

class UsersComment(Resource):
    def get(self):
        comments = CommentModel.query.all()
        return {"comments" : list(map(lambda u:u.jsonify(), comments))}


    parser = reqparse.RequestParser()
    parser.add_argument('comment',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('rating',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('movie_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('date',
                        type=datetime,
                        required=True,
                        help="This field cannot be blank."
                        )
    
    def post(self):
        data = UsersComment.parser.parse_args()

        if CommentModel.find_by_email(data['movie_id']):
            return {"message": "A user with that email  already exists"}, 400

        user = CommentModel(data['username'], data['password'], data['email'])
        user.save_to_db()
        

        return {"message": "User created successfully."}, 201