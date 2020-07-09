from app import app
from flask import render_template, redirect, url_for
from app.db import owners


@app.route('/')
def index():
    return redirect(url_for('owner.start'))
