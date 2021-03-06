from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('TEST_DB_URI')
app.config['SECRET_KEY']=getenv('TEST_SECRET_KEY')

db = SQLAlchemy(app)
