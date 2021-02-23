import unittest

class TestMethods(unittest.TestCase):

    def test_hello(self):
        """Teste les valeurs références."""
        #for value, expected in self.test_values:
        self.assertEqual('Hello, World', hello_world())

    def test_by_country(country):
        """Teste les valeurs références."""
        #for value, expected in self.test_values:
        country.assertEqual('[{"num": 8, "Country": "Albania", "Year": 2017, "Series": "Emissions (thousand metric tons of carbon dioxide)", "Value": 4342.011}]', by_country('Albania'))

if __name__ == '__main__':
    unittest.main()