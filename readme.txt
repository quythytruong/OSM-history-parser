Les différentes étapes pour charger les données OSM contenues dans un fichier historique osh.pbf dans une base de données PostgreSQL:
- Créer une base de données PostgreSQL en y ajoutant l'extension hstore (pour stocker les tags dans une colonne) et éventuellement PostGIS pour stocker des géométries par la suite
- Créer les tables de la base de données : lancer le script osm_creation_tables_avec_pk.sql
- Modifier les paramètres de connexion à la BD sur le fichier de configuration database.ini 
- Importer les données dans PostgreSQL avec Python : cf. TimeLineHandler.py
- Lancer la reconstruction des coordonnées extrêmes des ways : 
	- Dans le fichier way_geom_optimise_avec_index_geo_propre.sql, lancer PgScript sur la fonction way_geom (lignes 1 à 71)
	- Puis ajouter des colonnes à la table way, leurs index correspondants (lignes 73 à 87)
	- Lancer la requête "SELECT way_geom(idSerialDeb,idSerialFin);" pour remplir les coordonnées des lignes correspondantes
