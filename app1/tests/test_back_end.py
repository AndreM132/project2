import unittest, pytest

from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
from application import app, db
from application.models import Outfit
from os import getenv

class TestBase(TestCase):

    def create_app(self):

    
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()



class TestViews(TestBase):

    def test_homepage_view(self):
        with patch('requests.get') as h:
            h.return_value.text = "home"
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)

    def test_outfit_view(self):
        response = self.client.get(url_for('outfit'))
        self.assertEqual(response.status_code, 200)


