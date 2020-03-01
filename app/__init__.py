from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import random


app = Flask(__name__)
# security
app.config['SECRET_KEY'] = random._urandom(56)

# config Recaptcha for registeration paged
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = 'public'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'private'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}

# Mail configuration
app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'eranbolan91@gmail.com'
app.config['MAIL_PASSWORD'] = 'eranbolan1991'
app.config['MAIL_DEFAULT_SENDER'] = ('TallyBI','eranbolan@gmail.com')
app.config['MAIL_MAX_EMAILS'] = 10
app.config['MAIL_ASCII_ATTACHMENTS'] = False

# Database Connection
db_info = {'host': 'localhost',
           'database': 'tollybi',
           'psw': 'eranbolan',
           'user': 'postgres',
           'port': '5432'}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgres://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes