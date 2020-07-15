from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config.DevConfig')

owners_db = SQLAlchemy(app)
pets_db = SQLAlchemy(app)

from app.owner.views import owner
app.register_blueprint(owner, url_prefix='/owner')

from app import views
