from operator import add
from .. import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(
        db.Integer,
        primary_key=True,
        unique=True,
        nullable=False,
    )
    name = db.Column(
        db.String,
        primary_key=False,
        unique=False,
        nullable=True,
    )
    email = db.Column(
        db.String,
        primary_key=False,
        unique=False,
        nullable=True,
    )
    updated_at = db.Column(
        db.DateTime,
        primary_key=False,
        unique=False,
        nullable=True,
    )
    deleted_at = db.Column(
        db.DateTime,
        primary_key=False,
        unique=False,
        nullable=True,
    )

    def __init__(self, id=None, name=None, email=None, updated_at=None, deleted_at=None):
        self.id = id
        self.name = name
        self.email = email
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def select_one(self):
        return self.query.first()

    def select_all(self):
        return self.query.all()

    def select_by_id(self):
        return self.query.filter_by(id=self.id).all()
