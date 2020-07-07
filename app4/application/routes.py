from application import app, db
from flask import render_template, redirect, url_for, request, Flask, Response
from os import getenv
import requests
from flask_sqlalchemy import SQLAlchemy
from application.models import Outfit


@app.route('/', methods=['GET', 'POST'])
def outfit():
     brands = requests.get('http://app2:5001/').text
     clothes = requests.get('http://app3:5002/').text
     out = Outfit(
             brands = brands,
             clothes = clothes
     )
     db.session.add(out)
     db.session.commit()
     
     response = "You've got: " + brands + " " + clothes + ". " + "Congratulations!"
     return response

