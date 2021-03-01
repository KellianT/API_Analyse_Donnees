import unittest
from fonctions import voir_csv
from fonctions import country_inall_countries, year_inall_years
from fonctions import by_country_to_json, mean_to_json
from fonctions import per_capita_to_json
import pandas

df = voir_csv('onu.csv')




class TestMethods(unittest.TestCase):

    def test_voir_csv(self):

    """ Test if the CSV file is in pandas format
    and if the column "Country" is is the CSV """

        self.assertIsInstance(voir_csv('onu.csv'), pandas.core.frame.DataFrame)
        self.assertTrue("Country" in voir_csv('onu.csv'))




    def test_country_inall_countries(self):

        """ Check if the country exists in the CSV file
        with a country that exist and one that doesn't """

        self.assertTrue(country_inall_countries('france', df))
        self.assertFalse(country_inall_countries('Disneyland', df))

    def test_year_inall_years(self):

        """ Check if the year exists in the CSV file
        with a year that exists and one that doesn't""""

        self.assertTrue(year_inall_years(2015, df))
        self.assertFalse(year_inall_years(1974, df))

    def test_by_country_to_json(self):

        """Check if the valors are correct for the asked countries
        for the by_country function and if the result is in json format """
        
        self.assertEqual(by_country_to_json('Italy', df), {"Country": "Italy", "Year": 2017, "Value": 321481.224})
        self.assertEqual(by_country_to_json('Albania', df), {"Country": "Albania", "Year": 2017, "Value": 4342.011})
        self.assertIsInstance(by_country_to_json('France', df), dict)

    def test_mean_to_json(self):
        """Check if the valors are correct for the asked countries
        for the mean function and if the result is in json format."""

        self.assertEqual(mean_to_json('1975', df), {"year": "1975", "total": 112083.79604545454})
        self.assertEqual(mean_to_json('2015', df), {"year": "2015", "total": 217617.02909154928})
        self.assertIsInstance(mean_to_json('1970', df), dict)

    def test_per_capita_to_json(self):

        """Check if the valors are correct for the asked countries
        for the per_capita function and if the result is in json format."""

        self.assertIsInstance(per_capita_to_json('Benin', df), dict)
        self.assertTrue(1975 in per_capita_to_json('France', df))
        self.assertFalse(1974 in per_capita_to_json('France', df))

    


if __name__ == '__main__':
    unittest.main()
