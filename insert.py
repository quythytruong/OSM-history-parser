# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:07:32 2018

@author: Quy Thy
"""

import psycopg2
from config import config

def insert_node_list(node_list):
    """ insert a new OSM node into the node table """
    query = """INSERT INTO node(idnode, id, vnode, changeset, uid, username,
            datemodif, tags, visible, lat, lon)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(query, node_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception) as error:
        #print(error)
        #print(node_list)
        #file = open("D:/Users/qttruong/python-scripts/OSMmetadataAvecPython/node_list.txt","w")
        #file.write(str(node_list)) 
        #file.close() 
        pass
    finally:
        if conn is not None:
            conn.close()

def insert_way_list(way_list):
    """ insert a new OSM way into the way table """
    query = """INSERT INTO way (idway, id, vway, changeset, uid, username,
            datemodif, tags, visible, composedof)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(query, way_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception) as error:
        pass
#        print(error)
#        #print(node_list)
#        file = open("D:/Users/qttruong/python-scripts/OSMmetadataAvecPython/osm_list.txt","w")
#        file.write(str(way_list)) 
#        file.close() 
    finally:
        if conn is not None:
            conn.close()
            
def insert_relation_list(rel_list):
    """ insert a new OSM relation into the relation table """
    query = """INSERT INTO relation (idrel, id, vrel, changeset, uid, username,
            datemodif, tags, visible)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(query, rel_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception) as error:
        pass
#        print(error)
#        file = open("D:/Users/qttruong/python-scripts/OSMmetadataAvecPython/osm_list.txt","w")
#        file.write(str(rel_list)) 
#        file.close() 
    finally:
        if conn is not None:
            conn.close()
def insert_relationmb_list(relmb_list):
    """ insert a new OSM relation member into the relationmember table """
    query = """INSERT INTO relationmember (idrel, idmb, typemb, rolemb)
             VALUES(%s, %s, %s, %s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(query, relmb_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception) as error:
        pass
#        print(error)
#        #print(node_list)
#        file = open("D:/Users/qttruong/python-scripts/OSMmetadataAvecPython/osm_list.txt","w")
#        file.write(str(relmb_list)) 
#        file.close() 
    finally:
        if conn is not None:
            conn.close()