import unittest
from app_onu import app
# from flask import Flask


class TestAppFlask(unittest.TestCase):

    def test_home_status_code(self):
        ''' Function that allows us to retrieve the response code of the query
            sends HTTP GET request to the application
            on the specified path'''
        self.app = app.test_client()
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_hello_world(self):
        ''' Fonction basic test
            sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get('/')
        self.assertEqual(result.data, b'Hello, World')


class TestLatestByCountry(unittest.TestCase):

    def test_latest_by_country_status(self):
        ''' Function that allows us to retrieve the response code of the query
            sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/latest_by_country/France")
        self.assertEqual(result.status_code, 200)

    def test_latest_by_country_type(self):
        ''' sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/latest_by_country/France")
        self.assertEqual(result.content_type, "application/json")

    def test_latest_by_country_data(self):
        ''' verification of the data in the results '''
        self.app = app.test_client()
        result = self.app.get("/latest_by_country/France")
        self.assertTrue(b'Country' in result.data)


class TestAverageByYear(unittest.TestCase):

    def test_average_by_year_status(self):
        ''' Function that allows us to retrieve the response code of the query
            sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/average_by_year/2015")
        self.assertEqual(result.status_code, 200)

    def test_average_by_year_type(self):
        ''' verifies the type of data
            sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/average_by_year/2015")
        self.assertEqual(result.content_type, "application/json")

    def test_average_by_year_data(self):
        ''' verifies the type of data '''
        self.app = app.test_client()
        result = self.app.get("/average_by_year/2015")
        self.assertTrue(b'year' in result.data)


class TestPerCapits(unittest.TestCase):

    def test_per_capita_status(self):
        ''' sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/per_capita/France")
        self.assertEqual(result.status_code, 200)

    def test_per_capita_type(self):
        ''' sends HTTP GET request to the application
            on the specified path '''
        self.app = app.test_client()
        result = self.app.get("/per_capita/France")
        self.assertEqual(result.content_type, "application/json")

    def test_per_capita_data(self):
        self.app = app.test_client()
        result = self.app.get("/per_capita/France")
        self.assertTrue(b'2015' in result.data)


if __name__ == '__main__':
    unittest.main()
