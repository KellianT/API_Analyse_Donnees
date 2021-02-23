import json
import logging
import csv
import pandas as pd
import unittest
from flask import Flask, abort
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

<<<<<<< HEAD

board = pd.read_csv('onu.csv', header=1, usecols=['Region/Country/Area', 'Unnamed: 1', 'Value', 'Year', 'Series'])
=======
#url = 'https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv'
board = pd.read_csv('onu.csv', header = 1, usecols=['Region/Country/Area', 'Unnamed: 1', 'Value', 'Year', 'Series'])
>>>>>>> origin
db_onu = board.rename(columns={'Region/Country/Area': 'num', 'Unnamed: 1': 'Country'})


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
        parsed = json.loads(result)
        return json.dumps(parsed)

    else:

        print("erreur 404")
    #erreur 404 si on demande un pays qui n'est pas connu
    #     abort(404)
<<<<<<< HEAD


@app.route('/average_by_year/<year>')
def average_for_year(year):
    #on cherche la moyenne des émissions totales au niveau mondial pour une année demandée
    # logging.debug(f"Année demandée : {year}")
    all_years = list(set(db_onu['Year'].to_list()))
    if year in all_years:
        df = db_onu[(db_onu['Year'] == year) & (db_onu['Series'] == 'Emissions (thousand metric tons of carbon dioxide)')]
        mean_df = df.mean().round()['Value']
        return json.dumps({"year": "1975", "total": mean_df})
    else:
        #abort(404)
        print("c'est la zone")


if  __name__ == "__main__":
=======
# print(hello_world())
# print(by_country('ALBAnia'))

@app.route('/average_by_year/<year>')
def average_for_year(year):
    
    
    # file = open("onu.csv","r")
    # test=csv.reader(file)
    # for row in test:
    #     print(row[1])

    #on cherche la moyenne des émissions totales au niveau mondial pour une année demandée
    # logging.debug(f"Année demandée : {year}")
    all_years = list(set(db_onu['Year'].to_list()))
    #print(all_years)
    if year in all_years:
        df = db_onu[(db_onu['Year'] == year) & (db_onu['Series'] == 'Emissions (thousand metric tons of carbon dioxide)')]
        mean_df= df.mean().round()['Value']
        return json.dumps({"year":"1975", "total":mean_df})
    else:
        #abort(404)
        print("c'est la zone")
#print(average_for_year(2015))
if __name__ == "__main__":
>>>>>>> origin
    app.run()