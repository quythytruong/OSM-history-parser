# OSM-history-parser
Scripts for parsing and storing OSM history data into a PostgreSQL database

*** Step 1 : Database preparation ***
- Create a new PostgreSQL database
- Add plugins : hstore, postgis
- Create new empty tables : run osm_creation_tables_avec_pk.sql

*** Step 2 : Parsing and storing OSM data history with Python ***
- Configure Python connexion settings to Postgres database : modify database.ini file
- Import OSM data history into database : run TimeLineHandler.py

*** Step 3 : Way geometry reconstruction ***
In way_geom_optimise_avec_index_geo_propre.sql file :
- Execute way_geom function : execute PgScript on lines 1 to 71 
- Add lon_min, lat_min, lon_max, lat_max columns to table way : run lines 73 to 87 
- Run query "SELECT way_geom(idSerialDeb,idSerialFin);" to fill the coordinates of the rows which ID is in the interval idSerialDeb-idSerialFin
