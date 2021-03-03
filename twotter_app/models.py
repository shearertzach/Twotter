from twotter_app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin
import enum


class Twot(db.Model):
    """Twot Model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(140), nullable=False)
    publish_date = db.Column(db.Date)

    replies = db.relationship('Reply', back_populates='twot')
    user = db.relationship('User', back_populates='twot')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


twot_replies_table = db.Table('twot_replies',
    db.Column('twot_id', db.Integer, db.ForeignKey('twot.id')),
    db.Column('reply_id', db.Integer, db.ForeignKey('reply.id'))
)


class Reply(db.Model):
    """Reply Model"""
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140), nullable=False)
    publish_date = db.Column(db.Date)

    user = db.relationship('User', back_populates='replies')
    twot = db.relationship('Twot', back_populates='replies')



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    twots = db.relationship('Twot', back_populates='user')
    replies = db.relationship('Reply', back_populates='user')

    def __repr__(self):
        return f'<User: {self.username}>'

favorite_twots_table = db.Table('user_favorite_twots',
    db.Column('twot_id', db.Integer, db.ForeignKey('twot.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)