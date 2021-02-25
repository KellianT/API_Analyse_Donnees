import unittest
from app_onu import app
# from flask import Flask


class TestAppFlask(unittest.TestCase):

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.app = app.test_client()
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_hello_world(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.app = app.test_client()
        result = self.app.get('/')
        # assert the response data
        self.assertEqual(result.data, b'Hello, World')


class TestAverageByYear(unittest.TestCase):

    def test_average_by_year_status(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.app = app.test_client()
        result = self.app.get("/average_by_year/2015")
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_average_by_year_type(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.app = app.test_client()
        result = self.app.get("/average_by_year/2015")
        # assert the type of the response
        self.assertEqual(result.content_type, "application/json")

    def test_average_by_year_data(self):
        self.app = app.test_client()
        result = self.app.get("/average_by_year/2015")
        self.assertTrue(result.data, 'year')

# test complémetnaire sur une valeur précise (pas forcement pertinent)
    def test_average_by_year_specific_data(self):
        self.app = app.test_client()
        result = self.app.get("/average_by_year/2015")
        self.assertEqual(result.data, b'{"year":"2015","total":217617.02909154928}\n')


if __name__ == '__main__':
    unittest.main()
