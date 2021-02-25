import json
import logging
from flask import Flask, abort, jsonify
app = Flask(__name__)
import csv
import pandas
import unittest
import api_fonctions as fct

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello_world():
    #utilisé pour tester si l'app fonctionne bien
    return 'Hello, World'


@app.route('/latest_by_country/<country>')
def by_country(country):
    #on veut la valeur la plus récente des emissions totales pour le pays demandé
    logging.debug(f"Pays demandé : {country}")
    db_onu = fct.voir_csv("onu.csv")
    country = country.title()
    if fct.country_inall_countries(country, db_onu):
       bycountryjson = fct.by_country_to_json(country,db_onu)
       return jsonify(bycountryjson)
    else:
        abort(404)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    #on cherche la moyenne des émissions totales au niveau mondial pour une année demandée
    logging.debug(f"Année demandée : {year}")
    db_onu = fct.voir_csv("onu.csv")
    if fct.year_inall_years(year, db_onu):
        mean_value = fct.mean_to_json(year, db_onu)
        return jsonify(mean_value)
    else:
        abort(404)



@app.route('/per_capita/<country>')
def per_capita(country):
    logging.debug(f"Pays demandé : {country}")
    db_onu = fct.voir_csv("onu.csv")
    country = country.title()
    if fct.country_inall_countries(country, db_onu): 
        emissions_tojson = fct.per_capita_to_json(country, db_onu)
        return jsonify(emissions_tojson)
    else:
        #erreur 404 si on demande un pays qui n'est pas connu
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
