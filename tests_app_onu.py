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


class TestLatestByCountry(unittest.TestCase):

    def test_latest_by_country_status(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.app = app.test_client()
        result = self.app.get("/latest_by_country/France")
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_latest_by_country_type(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.app = app.test_client()
        result = self.app.get("/latest_by_country/France")
        # assert the type of the response
        self.assertEqual(result.content_type, "application/json")

    def test_latest_by_country_data(self):
        self.app = app.test_client()
        result = self.app.get("/latest_by_country/France")
        self.assertTrue(b'Country' in result.data)


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
        self.assertTrue(b'year' in result.data)


class TestPerCapits(unittest.TestCase):

    def test_per_capita_status(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.app = app.test_client()
        result = self.app.get("/per_capita/France")
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_per_capita_type(self):
        # sends HTTP GET request to the application
        # on the specified path
        self.app = app.test_client()
        result = self.app.get("/per_capita/France")
        # assert the type of the response
        self.assertEqual(result.content_type, "application/json")

    def test_per_capita_data(self):
        self.app = app.test_client()
        result = self.app.get("/per_capita/France")
        self.assertTrue(b'2015' in result.data)


if __name__ == '__main__':
    unittest.main()
