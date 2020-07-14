import unittest
  
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
from application import app, db
from application.models import Outfit
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
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

    def test_outfit_view(self):
        with patch('requests.post') as o:
            o.return_value.text = "Adidas"
            response = self.client.post(url_for('outfit'),data=dict(
                        brands="Adidas",
                        clothes="Tshirts"))
            self.assertIn(b"Adidas", response.data)

class TestApp(TestBase):
    def outfit_test(self):
        assert routes.outfit_test(brands,clothes) == "BAPE Tshirts"

        
    



