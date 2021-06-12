from datetime import datetime
from enum import unique

from .. import db


class MovieModel(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String())
    postor = db.Column(db.String(), default='movie.png', nullable=False)
    background = db.Column(db.String(), nullable=False, default='background.jpg')
    trailer = db.Column(db.String())
    screening = db.Column(db.String(), nullable=False) # default=datetime.utcnow
    genre = db.Column(db.String(), nullable=False)
    idmbRating = db.Column(db.Float, nullable=False, default=0.0)
    airedBy = db.Column(db.String(), nullable=False)
    release = db.Column(db.String(), nullable=False)
    ticket = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Movie('{self.title}')"

    def __init__(self, title, description, postor, background, trailer, screening, genre, idmbRating, airedBy, release, ticket):
        self.title = title
        self.postor = postor
        self.background = background
        self.description = description
        self.trailer = trailer
        self.screening = screening
        self.genre = genre
        self.idmbRating = idmbRating
        self.airedBy = airedBy
        self.release = release
        self.ticket = ticket
        
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        return {
            "title" : self.title,
            "description" : self.description,
            "postor" : self.postor,
            "background" : self.background,
            "trailer" : self.trailer,
            "screening" : self.screening,
            "genre" : self.genre,
            "idmbRating" : self.idmbRating,
            "airedBy" : self.airedBy,
            "release" : self.release,
            "ticket" : self.ticket,
        }

    