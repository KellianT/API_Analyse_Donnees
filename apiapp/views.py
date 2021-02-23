import json
import logging
from flask import Flask, abort
app = Flask(__name__)
import csv
import pandas
import unittest

logging.basicConfig(level=logging.DEBUG)

#url = 'https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv'
board = pandas.read_csv('onu.csv', header = 1, usecols=['Region/Country/Area', 'Unnamed: 1', 'Value', 'Year', 'Series'])
db_onu = board.rename(columns={'Region/Country/Area': 'num', 'Unnamed: 1': 'Country'})
#print(db_onu.head(1))

#def all_countries()
#    countries = list(set(df['Region'].to_list()))
#def par_pays (à appeler dans by_country)

@app.route('/')
def hello_world():
    #utilisé pour tester si l'app fonctionne bien
    return 'Hello, World'

@app.route('/latest_by_country/<country>')
def by_country(country):
    #on veut la valeur la plus récente des emissions totales pour le pays demandé
    #logging.debug(f"Pays demandé : {country}")
    country = country.title()
    countries = list(set(db_onu['Country'].to_list()))
    if country in countries:  
        country_emission = db_onu[(db_onu["Country"] == country) & (db_onu["Year"]==2017)].head(1)
        result = country_emission[['Country', 'Year', 'Value']].to_json(orient='records')
        #result = country_emission.to_json(orient='records')
        parsed = json.loads(result)
        return json.dumps(parsed) 
    #json.dumps({"country":"Albania","year":1975, "emissions":4338.3340})
    else:
        print("erreur 404")
    # #     #erreur 404 si on demande un pays qui n'est pas connu
    #     abort(404)
print(hello_world())
print(by_country('ALBAnia'))

if __name__ == "__main__":
    app.run()