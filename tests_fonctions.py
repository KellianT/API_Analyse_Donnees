import unittest
from fonctions import voir_csv, by_country_to_json, mean_to_json, per_capita_to_json

db_onu = voir_csv('onu.csv')

class TestMethods(unittest.TestCase):


    def test_by_country_to_json(self):
        """Teste les valeurs références."""
        self.assertEqual(by_country_to_json('Italy', db_onu), { "Country": "Italy", "Year": 2017, "Value": 321481.224 })
        self.assertEqual(by_country_to_json('Albania', db_onu), { "Country": "Albania", "Year": 2017, "Value": 4342.011 })
        self.assertIsInstance(by_country_to_json('France', db_onu), dict)

    def test_mean_to_json(self):
        """Teste les valeurs références."""
        self.assertEqual(mean_to_json('1975', db_onu), { "year": "1975", "total": 112083.79604545454 })
        self.assertEqual(mean_to_json('2015', db_onu), { "year": "2015", "total": 217617.02909154928 })
        self.assertIsInstance(mean_to_json('1970', db_onu), dict)


    def test_per_capita_to_json(self):
        """Teste les valeurs références."""
        self.assertIsInstance(per_capita_to_json('Benin', db_onu), dict)


if __name__ == '__main__':
    unittest.main()