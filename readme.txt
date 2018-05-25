Les diff�rentes �tapes pour charger les donn�es OSM contenues dans un fichier historique osh.pbf dans une base de donn�es PostgreSQL:
- Cr�er une base de donn�es PostgreSQL en y ajoutant l'extension hstore (pour stocker les tags dans une colonne) et �ventuellement PostGIS pour stocker des g�om�tries par la suite
- Cr�er les tables de la base de donn�es : lancer le script osm_creation_tables_avec_pk.sql
- Modifier les param�tres de connexion � la BD sur le fichier de configuration database.ini 
- Importer les donn�es dans PostgreSQL avec Python : cf. TimeLineHandler.py
- Lancer la reconstruction des coordonn�es extr�mes des ways : 
	- Dans le fichier way_geom_optimise_avec_index_geo_propre.sql, lancer PgScript sur la fonction way_geom (lignes 1 � 71)
	- Puis ajouter des colonnes � la table way, leurs index correspondants (lignes 73 � 87)
	- Lancer la requ�te "SELECT way_geom(idSerialDeb,idSerialFin);" pour remplir les coordonn�es des lignes correspondantes
