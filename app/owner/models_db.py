from app import owners_db, pets_db
from datetime import datetime


class Owners(owners_db.Model):
    id = owners_db.Column(owners_db.Integer, primary_key=True)
    name = owners_db.Column(owners_db.String(20))
    age = owners_db.Column(owners_db.Integer)
    city = owners_db.Column(owners_db.String(30))
    data_create = owners_db.Column(owners_db.DateTime, default=datetime.now)


class Pets(pets_db.Model):
    id = pets_db.Column(pets_db.Integer, primary_key=True)
    owner_id = pets_db.Column(pets_db.Integer)
    name = pets_db.Column(pets_db.String(50))
    age = pets_db.Column(pets_db.Integer)
    type = pets_db.Column(pets_db.String(40))
    data_create = pets_db.Column(pets_db.DateTime, default=datetime.now)
