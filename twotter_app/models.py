from twotter_app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin
import enum


class Twot(db.Model):
    """Twot Model"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280), nullable=False)
    publish_date = db.Column(db.Date)

    replies = db.relationship('Reply', back_populates='twot')


    user = db.relationship('User', back_populates='twots')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Reply(db.Model):
    """Reply Model"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(280), nullable=False)
    publish_date = db.Column(db.Date)

    user = db.relationship('User', back_populates='replies')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    
    twot = db.relationship('Twot', back_populates='replies')
    twot_id = db.Column(db.Integer, db.ForeignKey('twot.id'), nullable=False)



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    display_name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    twots = db.relationship('Twot', back_populates='user')
    replies = db.relationship('Reply', back_populates='user')

    def __repr__(self):
        return f'<User: {self.username}>'




favorite_twots_table = db.Table('user_favorite_twots',
    db.Column('twot_id', db.Integer, db.ForeignKey('twot.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)