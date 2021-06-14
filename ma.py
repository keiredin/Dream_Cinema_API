from flask_marshmallow import Marshmallow
from Dream_Cinema_API.models.user import *
from Dream_Cinema_API.models.movie import *
from Dream_Cinema_API.models.comment import *

ma = Marshmallow()


class MovieSchema(ma.Schema):
    class Meta:
        fields = ("Title", "Description","Postor", "Background","Trailer","Screening","Genre","IDMBRating", "AiredBy",
                  "ReleaseDate","Ticket")

        model = MovieModel


class UserSchema(ma.Schema):
    class Meta:
        fields = ("Username", "Email", "Password","Admin","Image","Twitter_link","Instagram_link")

        model = UserModel

class CommentSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "movie_id", "comment","rating","date")

        model = CommentModel