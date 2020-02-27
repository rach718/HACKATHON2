from app import db
from datetime import datetime


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.author_id'))
    pub_date = db.Column(db.DateTime, default=datetime.now, nullable=True)
    price = db.Column(db.Float, default=5.0)

    def __repr__(self):
        return f"<Book: {self.title}>"


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return self.name