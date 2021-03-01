# API_Analyse_Donnees
Développement d’une API d’analyse de données.

Bienvenue dans le ReadMe du groupe Yanis / Emilie / Kellian pour la promo 2020 de la formation Développeur Cloud ! 

Le but du brief était de développer une API d'analyse de données pour une ONG.

Cette API, réalisée avec Flask, nous permettra, à partir d'un fichier CSV fourni, de tirer parti des informations contenues à l'intérieur du fichier.
Ce fichier CSV contient plusieurs colonnes : 
    - l'ID du pays
    - le nom du pays
    - l'année de référence
    - les emissions de CO2 (global et par habitants)
    - la veleure de ces émissions
    - des notes sur le territoire
    - la source des informations

En l'occurence, le but était de développer 3 routes principales : 

   - /latest_by_country/<country> : nous permettra de récupérer la valeur des dernières emissions de CO2 par pays. Par exemple, pour la France, la requête se présentera sous la forme suivante : /latest_by_country/France qui nous retournera les informations demandées, à savoir l'année de référence (2017, date la plus récente dans le fichier CSV), la série correspondante (Thousand metric tons of carbon dioxide) ainsi que la valeur (ici, 306123.541).

   - /average_by_year/<year> : nous permettra de récupérer la moyenne des émissions de CO2 totale pour une année choisie. Par exemple, pour l'année 2015, la requête se présentera sous la forme suivante : /average_by_year/2015 qui nous retournera les informations demandées, à savoir l'année de référence (ici 2015) ainsi que la moyenne des émissions totales (ici, 217617.02909154928) calculées sur la série "Thousand metric tons of carbon dioxide)

   - /per_capita/<country> : nous permettra de récupérer la production de CO2 par habitant pour toutes les années associées au pays en question. Par exemple, pour l'Italie, la requête se présentera sous la forme suivante : /per_capita/Italy qui nous retournera les informations demandées, à savoir toutes les années associées (1975, 1985, 1995, 2005, 2010, 2015, 2016, 2017) ainsi que la valeur d'émissions en fonction de la série "Emissions per capita (metric tons of carbon dioxide)

IMPORTANT :

   Les requêtes seront à executées dans le navigateur WEB aprés lancement de l'API Flask. Le serveur étant hebergé localement pour cette exercice, la requête sur le navigateur prendra la forme suivante : http://127.0.0.1:5000/latest_by_country/France
    
   De plus, le format de retour de données associé au brief @Simplon se présente sous le format JSON.








