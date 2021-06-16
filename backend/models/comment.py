from backend.db import db
from datetime import datetime


class CommentModel(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False )
    movie_id = db.Column(db.Integer , db.ForeignKey('movies.id'), nullable=False )
    comment = db.Column(db.String(), nullable=False)
    rating = db.Column(db.Float)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # def __init__(self, user_id, movie_id, comment, rating, date):
    #     self.user_id = user_id
    #     self.comment = comment
    #     self.movie_id = movie_id
    #     self.comment = comment
    #     self.date = date

    def __repr__(self):
        return f"Comment('{self.comment}')"

    


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

#     @classmethod
#     def find_by_movie_id(cls, movie_id):
#         return cls.query.filter_by(movie_id=movie_id).first()

#     @classmethod
#     def find_by_id(cls, _id):
#         return cls.query.filter_by(id=_id).first()


#     def jsonify(self):
#         return {
#             "comment" : self.comment,
#             "rating" : self.rating,
#             "movie_id" : self.movie_id
#             "user_id" : self.user_id
#             "date" : self.date
#         }