import json
import logging
#from flask import Flask, abort
#app = Flask(__name__)
import csv
import pandas

logging.basicConfig(level=logging.DEBUG)

url = 'https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv'
board = pandas.read_csv(url, header = 1, usecols=['Region/Country/Area', 'Unnamed: 1', 'Value', 'Year'])
db_onu = board.rename(columns={'Region/Country/Area': 'num', 'Unnamed: 1': 'Country'})
print(db_onu.head(12))



if __name__=="__main__":
    app.run(debug=True)

