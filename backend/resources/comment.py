from flask.globals import request
from datetime import datetime
from flask_restplus import Resource,fields
from backend.models.comment import CommentModel
from backend.ma import *
from backend import api


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

class UsersComment(Resource):
    comment = api.model("Comment", {
        'user_id' : fields.Integer,
        'movie_id' : fields.Integer,
        'comment' : fields.String('The Comment'),
        'rating' : fields.Float,
        'date' : fields.DateTime
    })


    def get(self):
        '''
            Get all comments

        '''
        comments = CommentModel.query.all()
        return comments_schema.dump(comments)


    # parser = reqparse.RequestParser()
    # parser.add_argument('comment',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('rating',
    #                     type=float,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('user_id',
    #                     type=int,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('movie_id',
    #                     type=int,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('date',
    #                     type=datetime,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    
    @api.expect(comment)
    def post(self):
        '''
            Create a new comment

        '''
       
        new_comment = CommentModel()
        datejson = request.json['date']
        new_comment.user_id = request.json['user_id']
        new_comment.movie_id = request.json['movie_id']
        new_comment.comment = request.json['comment']
        new_comment.rating = request.json['rating']
        new_comment.date = datetime(int(datejson[:4]), int(datejson[5:7]), int(datejson[8:10]),int(datejson[11:13]), int(datejson[14:16]), int(datejson[17:19]))
        new_comment.save_to_db()
        
        return {"message": "Comment added successfully."}, 201

class UserComment(Resource):
    comment = api.model("Comment", {
        'user_id' : fields.Integer,
        'movie_id' : fields.Integer,
        'comment' : fields.String('The Comment'),
        'rating' : fields.Float,
        'date' : fields.DateTime
    })

    def get(self, id):
        '''
            Get a single comment

        '''
        comment = CommentModel.query.filter_by(id=id).first()

        if comment:
            return comment_schema.dump(comment),200
        return {"message": "Comment is not found!"}, 404

    def delete(self, id):
        '''
            Delete a comment from Database
        '''
        comment = CommentModel.query.filter_by(id=id).first()
        if comment:
            comment.delete_from_db()
            return {"message": "Comment is successfully deleted!"}, 200
        return {"message": "Comment is not found!"}, 404

    @api.expect(comment)
    def put(self, id):
        '''
            Update an existing comment
        '''

        commentToEdit = CommentModel.query.filter_by(id=id).first()
        # try :
        if commentToEdit:
            datejson = request.json['date']

            commentToEdit.comment = request.json['comment']
            commentToEdit.rating = request.json['rating']
            commentToEdit.date = datetime(int(datejson[:4]), int(datejson[5:7]), int(datejson[8:10]),int(datejson[11:13]), int(datejson[14:16]), int(datejson[17:19]))
            
            commentToEdit.save_to_db()
            return comment_schema.dump(commentToEdit), 200
        
        return {"message" : "Comment not found"}, 404
        # except:
        #     return {"message" : "Please Try Again"}