import json
import logging
import csv
import pandas
import unittest


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

    
