from flask import Flask
from app.owner.views import owner

app = Flask(__name__)

app.config.from_object('config.DevConfig')

app.register_blueprint(owner, url_prefix='/owner')

from app import views
