import logging
import pandas
# import json
# import csv
# import unittest


def voir_csv(csv):
    logging.info("création de la base de données")
    db_onu = pandas.read_csv(csv, header=2, names=['num', 'Country', 'Year', 'Emission', 'Value', 'Footnote', 'Source'])
    return db_onu


def country_inall_countries(country, db_onu):
    logging.info("vérification si le pays demandé existe")
    country = country.title()
    countries = list(set(db_onu['Country'].to_list()))
    if country in countries:
        return True
    else:
        return False


def year_inall_years(year, db_onu):
    logging.info("vérification si l'année demandée existe")
    all_years = list(set(db_onu['Year'].to_list()))
    if int(year) in all_years:
        return True
    else:
        return False


def by_country_to_json(country, db_onu):
    logging.info("création du dictionnaire dans fonction by_country_to_json")
    country_emission = db_onu[(db_onu["Country"] == country) & (db_onu["Year"] == 2017)].head(1)
    result = {}
    result['Country'] = str(country_emission.iloc[0][1])
    result['Year'] = int(country_emission.iloc[0][2])
    result['Value'] = float(country_emission.iloc[0][4])
    return result


def mean_to_json(year, db_onu):
    logging.info("création du dictionnaire dans fonction mean_to_json")
    df = db_onu.loc[db_onu['Year'].isin([year])]
    df = df[(df["Emission"] == 'Emissions (thousand metric tons of carbon dioxide)')]
    df_mean = df.mean()['Value']
    result = {}
    result['year'] = year
    result['total'] = df_mean
    return result


def per_capita_to_json(country, db_onu):
    logging.info("création du dictionnaire dans fonction per_capita_to_json")
    df_capita = db_onu[(db_onu["Country"] == country) & (db_onu["Emission"] == "Emissions per capita (metric tons of carbon dioxide)")]
    df_capita = df_capita[['Year', 'Value']]
    result = {}
    for i in range(len(df_capita)):
        key = int(df_capita.iloc[i][0])
        value = float(df_capita.iloc[i][1])
        result[key] = value
    return result
