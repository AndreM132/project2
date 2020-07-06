from application import app, db
from flask import render_template, redirect, url_for, request, Flask, Response
from os import getenv
import requests, random
from flask_sqlalchemy import SQLAlchemy
from application.models import Brands


@app.route('/', methods=['GET', 'POST'])
def brands():
    randombrands = random.randint(1, 10)
    getBrands = Brands.query.filter_by(id=randombrands).first()
    print(getBrands)

    return str(getBrands)
