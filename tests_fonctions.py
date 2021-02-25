import unittest
import pandas as pd
from fonctions import voir_csv
from fonctions import country_inall_countries, year_inall_years 
from fonctions import by_country_to_json, mean_to_json
from fonctions import per_capita_to_json

df = voir_csv('onu.csv')

class TestMethods(unittest.TestCase):

    

    def test_country_inall_countries(self):
        # country = country.title()
        # countries = list(set(db_onu['Country'].to_list()))
        self.assertTrue(country_inall_countries('france', df))

if __name__ == '__main__':
    unittest.main()