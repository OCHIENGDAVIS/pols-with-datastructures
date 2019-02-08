"""A module defining the Base Test Class"""
from unittest import TestCase
from app import create_app
from instance import config


class BaseTest(TestCase):
    """Base Test Class to every test class"""

    def setUp(self):
        """Set up the testing data and Test object attributes """
        app = create_app(config.DevelopmentConfig)
        self.app = app.test_client()
        self.app_context = app.app_context
        self.party_test_data = dict(
            id=1,
            name="Jubilee",
            hqAddress="Jubilee House",
            logoUrl="https:www.jubilee.co.ke/logo.png"
        )
        self.office_test_data = dict(
            id=1,
            type="Local government",
            name="Office of the MCA",
        )
