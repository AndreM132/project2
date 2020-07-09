import unittest
  
from flask import url_for
from flask_testing import TestCase

from application import app, db
from os import getenv

from application.models import Outfit

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

    def test_brands_view(self):
        response = self.client.get(url_for('brands'))
        self.assertEqual(response.status_code, 200)


class TestRepr(TestBase):
    def test_brands_repr(self):
        b = Brands()
        assert b == 'Test Brands'

