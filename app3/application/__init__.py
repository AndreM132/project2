from flask import Flask, request
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=getenv('OUTFIT_DB_URI')
app.config['SECRET_KEY'] = getenv('NEW_SECRET_KEY')
db = SQLAlchemy(app)


from application import routes

