import fonctions as fct
import logging
from flask import Flask, abort, jsonify, render_template,\
    request, url_for, flash, redirect
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(
    filename='app_onu.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',)


@app.route('/')
def hello_world():
    """ This function says 'Hello, World'. """
    # utilisé pour tester si l'app fonctionne bien
    return 'Hello, World'


@app.route('/latest_by_country/<country>')
def by_country(country):
    """ This function searches for country emissions
    (thousand metric tons of carbon dioxide) latest value.
    Parameter : a country (ex: France)
    Returns : json data
    Example :
    for France (127.0.0.1:5000/latest_by_country/France)
    {
    "Country": "France",
    "Year": 2017,
    "Value": 306123.541
    }
    """
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
    """ This function searches for average emissions
    (thousand metric tons of carbon dioxide) value for a set year.
    Parameter : a year (ex: 2015)
    Returns : json data
    Example :
    for 2015 (http://127.0.0.1:5000/average_by_year/2017)
    {
    "year": "2015",
    "total": 217617.02909154928
    }
    """
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
    """ This function shows for country emissions
    per capita (metric tons of carbon dioxide) values.
    Parameter : a country (ex: Italy)
    Returns : json data
    Example :
    for Italy (http://127.0.0.1:5000/per_capita/ITALY)
    {
    "1975": 5.719,
    "1985": 6.044,
    "1995": 7.056,
    "2005": 7.844,
    "2010": 6.552,
    "2015": 5.428,
    "2016": 5.371,
    "2017": 5.31
    }
    """
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
