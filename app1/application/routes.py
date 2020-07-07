from application import app, db
from flask import render_template, redirect, url_for, request, Flask
from os import getenv
import requests
from flask_sqlalchemy import SQLAlchemy
from application.models import Outfit


@app.route('/', methods=['GET'])
@app.route('/home')
def home():
        response = requests.get('http://app4:5003/').text
        return render_template('home.html', display=response, title='Home')

@app.route('/outfit')
def outfit():
    OutfitData = Outfit.query.all()
    return render_template('outfit.html', outfit=OutfitData, title='Brands and Clothes')




