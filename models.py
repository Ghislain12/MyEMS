from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, TIMESTAMP
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    birthdate = db.Column(db.String(30))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    gender = db.Column(db.Boolean)
    avatar = db.Column(db.String(500))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    year = db.relationship('Year', uselist=False, backref='user')
    role = db.Column(db.Boolean, default=False, nullable=False)
    account_status = db.Column(db.Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('roles', lazy='dynamic'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class Year(db.Model):
    __tablename__ = 'year'

    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
