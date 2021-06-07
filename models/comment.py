from db import db
from datetime import datetime
from enum import unique


class Comment(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'),nullable=False )
    movie_id = db.Column(db.Integer , db.ForeignKey('movies.id'), nullable=False )
    comment = db.Column(db.String(), nullable=False)
    rating = db.Column(db.Float)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Comment('{self.comment}')"