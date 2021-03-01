# API_Analyse_Donnees
Développement d’une API d’analyse de données.

Bienvenue dans le ReadMe du groupe Yanis / Emilie / Kellian pour la promo 2020 de la formation Développeur Cloud ! 

Le but du brief était de développer une API d'analyse de données pour une ONG.

Cette API, réalisée avec Flask, nous permettra, à partir d'un fichier CSV fourni, de tirer parti des informations contenues à l'intérieur du fichier téléchargable sur le site de l'ONU(https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv)

Ce fichier CSV contient plusieurs colonnes : 
   - l'ID du pays
   - le nom du pays
   - l'année de référence
   - les emissions de CO2 (global et par habitants)
   - la valeur de ces émissions
   - des notes sur le territoire
   - la source des informations

En l'occurence, le but était de développer 3 routes principales : 

   - /latest_by_country/<country> : nous permettra de récupérer la valeur des dernières emissions de CO2 par pays. Par exemple, pour la France, la requête se présentera sous la forme suivante : /latest_by_country/France qui nous retournera les informations demandées, à savoir l'année de référence (2017, date la plus récente dans le fichier CSV), la série correspondante (Thousand metric tons of carbon dioxide) ainsi que la valeur (ici, 306123.541).

   - /average_by_year/<year> : nous permettra de récupérer la moyenne des émissions de CO2 totale pour une année choisie. Par exemple, pour l'année 2015, la requête se présentera sous la forme suivante : /average_by_year/2015 qui nous retournera les informations demandées, à savoir l'année de référence (ici 2015) ainsi que la moyenne des émissions totales (ici, 217617.02909154928) calculées sur la série "Thousand metric tons of carbon dioxide)

   - /per_capita/<country> : nous permettra de récupérer la production de CO2 par habitant pour toutes les années associées au pays en question. Par exemple, pour l'Italie, la requête se présentera sous la forme suivante : /per_capita/Italy qui nous retournera les informations demandées, à savoir toutes les années associées (1975, 1985, 1995, 2005, 2010, 2015, 2016, 2017) ainsi que la valeur d'émissions en fonction de la série "Emissions per capita (metric tons of carbon dioxide)

IMPORTANT :

   Les requêtes seront à executées dans le navigateur WEB aprés lancement de l'API Flask. Le serveur étant hebergé localement pour cette exercice, la requête sur le navigateur prendra la forme suivante : http://127.0.0.1:5000/latest_by_country/France
    
   De plus, le format de retour de données associé au brief @Simplon se présente sous le format JSON.
   
   
  STRUCTURE DE L'API:
  
  Notre API se compose de
   
  METHODE DE TEST:
  
Nous avons choisis de séparer nos fichiers de test. Nous dispons d'un fichier contenant les test relatifs à l'API



Le fichier tests_app_onu.py teste les trois routes principales; Pour chaque route, les tests unitaires sont: 
- le code de retour de la requête (vérification que la requête renvoie 200)
- le type des données retournées (json)
- la présence d'un mot précis contenu dans les données retournées (ex: pour la route 'latest_by_country', vérification de la présence du mot 'Country')


Le fichier tests_fonctions.py teste toutes les fonctions appelées dans le fichiers app_onu.py. (voir documentation pour plus de détails)



