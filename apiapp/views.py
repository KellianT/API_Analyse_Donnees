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
db_onu = voir_csv("onu.csv")


@app.route('/')
def hello_world():
    #utilisé pour tester si l'app fonctionne bien
    return 'Hello, World'

@app.route('/latest_by_country/<country>')
def by_country(country):
    #on veut la valeur la plus récente des emissions totales pour le pays demandé
    logging.debug(f"Pays demandé : {country}")
    db_onu = voir_csv("onu.csv")
    if country_inall_countries(country, db_onu):
       bycountryjson = by_country_pandas(country,db_onu)
       return bycountryjson
    else:
        print("erreur 404")


def country_inall_countries(country,db_onu):
    country = country.title()
    countries = list(set(db_onu['Country'].to_list()))
    if country in countries:
        return True
    else:
        return False


def by_country_pandas(country,db_onu):
    country_emission = db_onu[(db_onu["Country"] == country) & (db_onu["Year"]==2017)].head(1)
    result = country_emission[['Country', 'Year', 'Value']].to_json(orient='records')
    parsed = json.loads(result)
    return json.dumps(parsed)

#print(by_country_pandas('Albania',db_onu))

#print(hello_world())
#print(by_country('ALBAnia'))

def all_years(year, db_onu):
    all_years = list(set(db_onu['Year'].to_list()))
    if int(year) in all_years: 
        return True
    else: 
        return False

def mean_to_json(year, db_onu): 
    df = db_onu.loc[db_onu['Year'].isin([year])]
    df = df[(df["Emission"]=='Emissions (thousand metric tons of carbon dioxide)')]
    df_mean = df.mean()['Value']
    result = {}
    result['year'] = year
    result['total'] = df_mean
    return json.dumps(result)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    #on cherche la moyenne des émissions totales au niveau mondial pour une année demandée
    logging.debug(f"Année demandée : {year}")
    if all_years(year, db_onu):
        mean_value = mean_to_json(year, db_onu)
        return mean_value
    else:
        print("erreur 404")



@app.route('/per_capita/<country>')
def per_capita(country):
    logging.debug(f"Pays demandé : {country}")
    country = country.title()
    countries = list(set(db_onu['Country'].to_list()))
    if country in countries: 
        df_capita = db_onu[(db_onu["Country"] == country) & (db_onu["Emission"]=="Emissions per capita (metric tons of carbon dioxide)")]  
        df_capita = df_capita[['Year', 'Value']]
        print(df_capita)
        result = df_capita.to_json(orient='records')
        parsed = json.loads(result)
        return json.dumps(parsed)
    else:
        #erreur 404 si on demande un pays qui n'est pas connu
        abort(404)
#print(per_capita('Albania'))

if __name__ == "__main__":
    app.run(debug=True)




''' #def all_countries()
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
    app.run() '''