from application import app, db
from flask import render_template, redirect, url_for, request, Flask, Response
from os import getenv
import requests, random
from flask_sqlalchemy import SQLAlchemy
from application.models import Clothes


@app.route('/', methods=['GET', 'POST'])
def clothes():
    randombrands = random.randint(1, 10)
    getClothes = Clothes.query.filter_by(id=randomclothes).first()
    print(getClothes)
    
    return str(getClothes)



