from datetime import datetime
from enum import unique

from db import db


class MovieModel(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String())
    postor = db.Column(db.String(), default='movie.png', nullable=False)
    background = db.Column(db.String(), nullable=False, default='background.jpg')
    trailer = db.Column(db.String())
    screening = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    genre = db.Column(db.String(), nullable=False)
    idmbRating = db.Column(db.Float, nullable=False, default=0.0)
    airedBy = db.Column(db.String(), nullable=False)
    release = db.Column(db.DateTime, nullable=False)
    ticket = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}')"

    