import unittest
import views

class TestMethods(unittest.TestCase):

    def test_hello(self):
        """Teste les valeurs références."""
        #for value, expected in self.test_values:
        self.assertEqual('Hello, World', views.hello_world())


    def test_by_country(country):
        """Teste les valeurs références."""
        #for value, expected in self.test_values:
        country.assertEqual('[{"Country": "Albania", "Year": 2017, "Value": 4342.011}]', views.by_country('Albania'))

        

if __name__ == '__main__':
    unittest.main()