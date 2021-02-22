import json
import logging
from flask import Flask, abort
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

"""
Récupérer les infos du fichier :
https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv
"""



if __name__=="__main__":
    app.run(debug=True)