import unittest
from app_onu import per_capita, by_country, average_for_year, hello_world

class TestMethods(unittest.TestCase):

    def test_hello(self):
        """Teste les valeurs références."""
        #for value, expected in self.test_values:
        self.assertEqual('Hello, World', hello_world())
        



    def test_by_country(self):
        """Teste les valeurs références."""
        #for value, expected in self.test_values:
        self.assertTrue('[{"Country": "Albania", "Year": 2017, "Value": 4342.011}]', by_country('Albania'))
       


    def test_per_capita(self):
        """ Test la fonction Per_Capita"""
        self.assertTrue('[{"Year": 1995, "Value": 7.845}, {"Year": 1985, "Value": 6.209}, {"Year": 1995, "Value": 5.773}, {"Year": 2005, "Value": 5.887}, {"Year": 2010, "Value": 5.233}, {"Year": 2015, "Value": 4.5}, {"Year": 2016, "Value": 4.515}, {"Year": 2017, "Value": 4.565}]', per_capita('France'))
        



if __name__ == '__main__':
    unittest.main()