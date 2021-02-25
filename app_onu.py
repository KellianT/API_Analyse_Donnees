import fonctions as fct
import logging
from flask import Flask, abort, jsonify
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# import csv
# import json
# import pandas
# import unittest

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(
    filename='app_onu.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',)


@app.route('/')
def hello_world():
    # utilisé pour tester si l'app fonctionne bien
    return 'Hello, World'


@app.route('/latest_by_country/<country>')
def by_country(country):
    # valeur la plus récente des emissions totales pour le pays demandé
    logging.info(f"Pays demandé : {country}")
    db_onu = fct.voir_csv("onu.csv")
    country = country.title()
    if fct.country_inall_countries(country, db_onu):
        bycountryjson = fct.by_country_to_json(country, db_onu)
        return jsonify(bycountryjson)
    else:
        logging.warning("erreur 404: fonction by_country")
        abort(404)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    # moyenne des émissions mondiales totales pour une année demandée
    logging.info(f"Année demandée : {year}")
    db_onu = fct.voir_csv("onu.csv")
    if fct.year_inall_years(year, db_onu):
        mean_value = fct.mean_to_json(year, db_onu)
        return jsonify(mean_value)
    else:
        logging.warning("erreur 404: fonction average_by_year")
        abort(404)


@app.route('/per_capita/<country>')
def per_capita(country):
    # toutes les emissions per capita pour un pays donné
    logging.info(f"Pays demandé : {country}")
    db_onu = fct.voir_csv("onu.csv")
    country = country.title()
    if fct.country_inall_countries(country, db_onu):
        emissions_tojson = fct.per_capita_to_json(country, db_onu)
        return jsonify(emissions_tojson)
    else:
        logging.warning("erreur 404; fonction per_capita")
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
