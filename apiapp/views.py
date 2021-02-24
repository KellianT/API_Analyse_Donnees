import json
import logging
from flask import Flask, abort
app = Flask(__name__)
import csv
import pandas
import unittest

logging.basicConfig(level=logging.DEBUG)

def voir_csv(csv):
    db_onu = pandas.read_csv(csv, header = 2, names = [ 'num','Country', 'Year','Emission','Value','Footnote','Source'])
    return db_onu


def country_inall_countries(country,db_onu):
    country = country.title()
    countries = list(set(db_onu['Country'].to_list()))
    if country in countries:
        return True
    else:
        return False

def year_inall_years(year, db_onu):
    all_years = list(set(db_onu['Year'].to_list()))
    if int(year) in all_years: 
        return True
    else: 
        return False


def by_country_to_json(country,db_onu):
    country_emission = db_onu[(db_onu["Country"] == country) & (db_onu["Year"]==2017)].head(1)
    result = country_emission[['Country', 'Year', 'Value']].to_json(orient='records')
    parsed = json.loads(result)
    return json.dumps(parsed)


def mean_to_json(year, db_onu): 
    df = db_onu.loc[db_onu['Year'].isin([year])]
    df = df[(df["Emission"]=='Emissions (thousand metric tons of carbon dioxide)')]
    df_mean = df.mean()['Value']
    result = {}
    result['year'] = year
    result['total'] = df_mean
    return json.dumps(result)

def per_capita_to_json(country, db_onu):
    df_capita = db_onu[(db_onu["Country"] == country) & (db_onu["Emission"]=="Emissions per capita (metric tons of carbon dioxide)")]  
    df_capita = df_capita[['Year', 'Value']]
    result = df_capita.to_json(orient='records')
    parsed = json.loads(result)
    return json.dumps(parsed)


@app.route('/')
def hello_world():
    #utilisé pour tester si l'app fonctionne bien
    return 'Hello, World'


@app.route('/latest_by_country/<country>')
def by_country(country):
    #on veut la valeur la plus récente des emissions totales pour le pays demandé
    logging.debug(f"Pays demandé : {country}")
    db_onu = voir_csv("onu.csv")
    country = country.title()
    if country_inall_countries(country, db_onu):
       bycountryjson = by_country_to_json(country,db_onu)
       return bycountryjson
    else:
        abort(404)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    #on cherche la moyenne des émissions totales au niveau mondial pour une année demandée
    logging.debug(f"Année demandée : {year}")
    db_onu = voir_csv("onu.csv")
    if year_inall_years(year, db_onu):
        mean_value = mean_to_json(year, db_onu)
        return mean_value
    else:
        abort(404)



@app.route('/per_capita/<country>')
def per_capita(country):
    logging.debug(f"Pays demandé : {country}")
    db_onu = voir_csv("onu.csv")
    country = country.title()
    if country_inall_countries(country, db_onu): 
        emissions_tojson = per_capita_to_json(country, db_onu)
        return emissions_tojson
    else:
        #erreur 404 si on demande un pays qui n'est pas connu
        abort(404)



if __name__ == "__main__":
    app.run(debug=True)
