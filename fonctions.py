import logging
import pandas


def voir_csv(csv):

    """This function return the CSV file in Pandas data format """

    logging.info("création de la base de données")
    db_onu = pandas.read_csv(csv, header=2, names=['num', 'Country', 'Year',
                                                   'Emission', 'Value',
                                                   'Footnote', 'Source'])
    return db_onu


def country_inall_countries(country, db_onu):
    """ This function checks whether the set country
    is included into the database (db_onu).
    Parameter : a country (ex: Albania), a database
    Returns : True or Flase
    Example : Albania returns True, Dysneyland returns False
    """
    logging.info("vérification si le pays demandé existe")
    country = country.title()
    countries = list(set(db_onu['Country'].to_list()))
    if country in countries:
        return True
    else:
        return False


def year_inall_years(year, db_onu):
    """ This function checks whether the set year
    is included into the database (db_onu).
    Parameter: a year (ex: 2015), a database
    Returns : True or Flase
    Example : 2015 returns true, 1974 returns false
    """
    logging.info("vérification si l'année demandée existe")
    all_years = list(set(db_onu['Year'].to_list()))
    if int(year) in all_years:
        return True
    else:
        return False


def by_country_to_json(country, db_onu):
    """ This function searches for country emissions
    (thousand metric tons of carbon dioxide) latest value.
    Parameter : a country (ex: France), a database
    Returns : a dictionnary
    Example : for France returns
    {"Country": "France", "Year": 2017, "Value": 306123.541}
    """
    logging.info("création du dictionnaire dans fonction by_country_to_json")
    country_emission = db_onu[(db_onu["Country"] == country) &
                              (db_onu["Year"] == 2017)].head(1)
    result = {}
    result['Country'] = str(country_emission.iloc[0][1])
    result['Year'] = int(country_emission.iloc[0][2])
    result['Value'] = float(country_emission.iloc[0][4])
    return result


def mean_to_json(year, db_onu):
    """ searches for average emissions
    (thousand metric tons of carbon dioxide) value for a set year.
    Parameter : a year (ex: 2015)
    Returns : a dictionnary
    Example : for 2015
    {"year": "2015", "total": 217617.02909154928}
    """
    logging.info("création du dictionnaire dans fonction mean_to_json")
    df = db_onu.loc[db_onu['Year'].isin([year])]
    df = df[(df["Emission"] ==
            'Emissions (thousand metric tons of carbon dioxide)')]
    df_mean = df.mean()['Value']
    result = {}
    result['year'] = year
    result['total'] = df_mean
    return result


def per_capita_to_json(country, db_onu):
    """ This function shows for country emissions
    per capita (metric tons of carbon dioxide) values.
    Parameter : a country (ex: Italy)
    Returns : a dictionnary
    Example : for Italy returns
    { "1975": 5.719, "1985": 6.044, "1995": 7.056, "2005": 7.844,
    "2010": 6.552, "2015": 5.428, "2016": 5.371, "2017": 5.31}
    """
    logging.info("création du dictionnaire dans fonction per_capita_to_json")
    df_capita = db_onu[(db_onu["Country"] ==
                        country) & (db_onu["Emission"] == "Emissions per capita (metric tons of carbon dioxide)")]
    df_capita = df_capita[['Year', 'Value']]
    result = {}
    for i in range(len(df_capita)):
        key = int(df_capita.iloc[i][0])
        value = float(df_capita.iloc[i][1])
        result[key] = value
    return result
