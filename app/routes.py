from app import app
from flask import render_template
from app import db



app.config['SECRET_KEY'] = 'no-corona-here'


@app.route('/')
def home():
    return render_template('home.html')
