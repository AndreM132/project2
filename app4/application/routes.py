from application import app, db
from flask import render_template, redirect, url_for, request, Flask, Response
from os import getenv
import requests
from flask_sqlalchemy import SQLAlchemy
from application.models import Outfit


@app.route('/', methods=['GET', 'POST'])
def outfit():
     brands = requests.get('http://service2:5001/').text
     clothes = requests.get('http://service2:5002/').text
     out = Outfit(
             brands = brands,
             clothes = clothes
     )
     db.session.add(out)
     db.session.commit()
     
     line = brands + " " + "and" + " " + clothes
     return line

