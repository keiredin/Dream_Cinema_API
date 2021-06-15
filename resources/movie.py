from Dream_Cinema_API.models.movie import MovieModel
from datetime import datetime
from flask_restplus import Resource, reqparse, fields
from flask import jsonify, request

from flask_jwt import *
from Dream_Cinema_API.ma import *
from Dream_Cinema_API import api



# class MovieSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'title', 'description', 'postor', 'background', 'trailer', 'screening', 'genre', 'idmbRating', 'airedBy', 'release', 'ticket')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

class MovieList(Resource):
    # # @jwt_required


    # Model required by flask_restplus for expect
    movieModel = api.model("MovieModel", {
        'Title': fields.String('Name of the Movie'),
        'Description': fields.String,
        'Postor' : fields.String('Poster url'),
        'Background': fields.String('Background url'),
        'Trailer': fields.String('trailer url'),
        'Screening': fields.DateTime,
        'Genre': fields.String,
        'IDMBRating': fields.Float,
        'AiredBy': fields.String,
        'ReleaseDate': fields.DateTime,
        'Ticket' : fields.String

    })
    # def get(self):
    #     movies = MovieModel.query.all()
    #     result = movies_schema.dump(movies)
    #     return jsonify(result.data)

    

    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('postor',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('background',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('trailer',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('screening',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )  
    parser.add_argument('genre',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('idmbRating',
                        type=float,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('airedBy',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        ) 
    parser.add_argument('release',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        ) 
    parser.add_argument('ticket',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )   


    def post(self):
        data = MovieList.parser.parse_args()

        if MovieModel.find_by_title(data['title']):
            return {"message": "A user with that title already exists"}, 400

        user = MovieModel(title=data['title'], description=data['description'], postor=data['postor'], background=data['background'], trailer=data['trailer'], screening=data['screening'], genre=data['genre'], idmbRating=data['idmbRating'], airedBy=data['airedBy'], release=data['release'], ticket=data['ticket'])
        user.save_to_db()
        

        return {"message": "User created successfully."}, 201

# class Movie(Resource):
#     def get(self, id):
#         movie = MovieModel.find_by_id(id)
#         if movie:
#             return {f"movie {movie.id}" : movie.json()}, 200
#         return {"message": "User is not found!"}, 404

    

