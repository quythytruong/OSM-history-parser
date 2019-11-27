﻿DROP TABLE IF EXISTS node, way, relation, relationmember;
/* Creates OSM nodes table */
CREATE TABLE node (
idnode BIGINT PRIMARY KEY, -- idnode is composed of id + vnode
id BIGINT,
vnode INTEGER,
changeset INTEGER,
username VARCHAR,
uid BIGINT,
datemodif TIMESTAMP WITH TIME ZONE,
tags HSTORE,
visible BOOLEAN,
lat NUMERIC,
lon NUMERIC
);
CREATE INDEX id_idx ON node (id);

/* Creates OSM ways table */
CREATE TABLE way (
idway BIGINT PRIMARY KEY, -- idway is composed of id + vway
id BIGINT,
vway INTEGER,
changeset INTEGER,
uid BIGINT,
username VARCHAR,
datemodif TIMESTAMP WITH TIME ZONE,
tags HSTORE,
visible BOOLEAN,
composedof BIGINT[] -- array of the nodes that compose the way
);
CREATE INDEX id_way_idx ON way (id);

/* Creates OSM relations table */
CREATE TABLE relation (
idrel BIGINT PRIMARY KEY, -- idrel is composed of id + vrel
id BIGINT,
vrel INTEGER,
changeset INTEGER,
uid BIGINT,
username VARCHAR,
datemodif TIMESTAMP WITH TIME ZONE,
tags HSTORE,
visible BOOLEAN);
CREATE INDEX id_relation_idx ON relation (id);

DROP TABLE IF EXISTS relationmember;
CREATE TABLE relationmember (
idrel BIGINT,-- idrel is composed of id + vrel
idmb BIGINT,
--idrelmb VARCHAR,-- idrelmb is composed of idrel + idmb
typemb VARCHAR, -- member type: node, way, or relation. The column values either 'n', 'w' or 'r'.
rolemb VARCHAR -- member role in the relation : outer or inner in case of a multipolygon relation
);
CREATE INDEX idmb_idx ON relationmember (idmb);
