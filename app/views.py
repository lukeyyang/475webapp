from app import app
from flask import render_template
from .nav import nav

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
