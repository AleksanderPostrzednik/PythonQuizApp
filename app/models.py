from flask_sqlalchemy import SQLAlchemy
from . import db

class UserResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, score):
        self.score = score