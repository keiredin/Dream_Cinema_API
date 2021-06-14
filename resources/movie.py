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
    movie = api.model("Movie", {
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

    def get(self):
        ''' 
            Get All Movies from the Database
        '''
        movies = MovieModel.query.all()
        return movies_schema.dump(movies)

    

    # parser = reqparse.RequestParser()
    # parser.add_argument('title',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('description',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('postor',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('background',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )

    # parser.add_argument('trailer',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )

    # parser.add_argument('screening',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )  
    # parser.add_argument('genre',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )

    # parser.add_argument('idmbRating',
    #                     type=float,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )
    # parser.add_argument('airedBy',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     ) 
    # parser.add_argument('release',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     ) 
    # parser.add_argument('ticket',
    #                     type=str,
    #                     required=True,
    #                     help="This field cannot be blank."
    #                     )   

    @api.expect(movie)
    def post(self):
        '''
            Create a new movie
        '''

        new_movie = MovieModel()
        scdate = request.json['Screening']
        reldate = request.json['ReleaseDate']
        new_movie.Title = request.json['Title']
        new_movie.Description = request.json['Description']
        new_movie.Postor = request.json['Postor']
        new_movie.Background = request.json['Background']
        new_movie.Trailer = request.json['Trailer']
        new_movie.Screening = datetime(int(scdate[:4]), int(scdate[5:7]), int(scdate[8:10]),int(scdate[11:13]), int(scdate[14:16]), int(scdate[17:19]))
        new_movie.Genre = request.json['Genre']
        new_movie.IDMBRating = request.json['IDMBRating']
        new_movie.AiredBy = request.json['AiredBy']
        new_movie.ReleaseDate = datetime(int(reldate[:4]), int(reldate[5:7]), int(reldate[8:10]),int(reldate[11:13]), int(reldate[14:16]), int(reldate[17:19]))
        new_movie.Ticket = request.json['Ticket']

        new_movie.save_to_db()
        return movie_schema.dump(new_movie), 201

class Movie(Resource):

    movie = api.model("Movie", {
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

    def get(self, id):
        '''
            Get a movie by id
        '''
        movie = MovieModel.find_by_id(id)
        if movie:
            return movie_schema.dump(movie),200
        return {"message": "Movie is not found!"}, 404

    @api.expect(movie)
    def put(self, id):
        '''
            Update an existing movie
        '''

        movieToEdit = MovieModel().query.filter_by(id=id).first()
        try :
            if movieToEdit:
                scdate = request.json['Screening']
                reldate = request.json['ReleaseDate']

                movieToEdit.Title = request.json['Title']
                movieToEdit.Description = request.json['Description']
                movieToEdit.Postor = request.json['Postor']
                movieToEdit.Background = request.json['Background']
                movieToEdit.Trailer = request.json['Trailer']
                movieToEdit.Screening = datetime(int(scdate[:4]), int(scdate[5:7]), int(scdate[8:10]),int(scdate[11:13]), int(scdate[14:16]), int(scdate[17:19]))
                movieToEdit.Genre = request.json['Genre']
                movieToEdit.IDMBRating = request.json['IDMBRating']
                movieToEdit.AiredBy = request.json['AiredBy']
                movieToEdit.ReleaseDate = datetime(int(reldate[:4]), int(reldate[5:7]), int(reldate[8:10]),int(reldate[11:13]), int(reldate[14:16]), int(reldate[17:19]))
                movieToEdit.Ticket = request.json['Ticket']

                movieToEdit.save_to_db()
                return movie_schema.dump(movieToEdit), 200
            
            return {"message" : "Movie not found"}, 404
        except:
            return {"message" : "Please Try Again"}

    def delete(self, id):
        '''
            Delete a movie from Database
        '''
        movie = MovieModel.find_by_id(id)
        if movie:
            movie.delete_from_db()
            return {"message": "Movie is successfully deleted!"}, 200
        return {"message": "Movie is not found!"}, 404

    

