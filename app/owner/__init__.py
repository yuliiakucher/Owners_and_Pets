from flask import Blueprint

owner = Blueprint('owner', __name__, static_folder='static', template_folder='templates')