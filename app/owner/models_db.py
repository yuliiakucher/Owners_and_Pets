from app import db
from datetime import datetime


class Owners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    city = db.Column(db.String(30))
    pets = db.relationship('Pets', backref='owner')
    data_create = db.Column(db.DateTime, default=datetime.now)


class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    type = db.Column(db.String(40))
    data_create = db.Column(db.DateTime, default=datetime.now)


