# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:07:32 2018

@author: Quy Thy
"""

import osmium as osm
import insert
from datetime import datetime
#import postgresql.string as re
#import pandas as pd

class TimelineHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.relationmblist = []
        self.relationlist = []
        self.waylist = []
        self.nodelist = []
        

    def node(self, n):
        idnode = str(n.id)+str(n.version)
        taghstore = ""
        for t in n.tags:
            #print(t.k.replace('"','\"').replace('\\', '\\\\'))
            #print(t.v.replace('"','\"').replace('\\', '\\\\'))
            taghstore += "\""+t.k.replace('\\', '\\\\').replace('"','\\"')+"\"=>\""+t.v.replace('\\', '\\\\').replace('"','\\"')+"\","
        taghstore = taghstore[:-1] # remove the last comma
        
        if n.location.valid():
            self.nodelist.append((idnode, n.id, n.version, n.changeset, n.uid,
                            n.user.replace('\\', '\\\\').replace('"','\\"'),
                            n.timestamp, taghstore, n.visible, n.location.lat, n.location.lon))
        else:
            # if node is not visible then location (lat/lon) values -2000
            self.nodelist.append((idnode, n.id, n.version, n.changeset, n.uid,
                             n.user.replace('\\', '\\\\').replace('"','\\"'), n.timestamp, taghstore,n.visible,-2000,-2000))
                
        #print(str(len(self.nodelist)))
        if len(self.nodelist) == 10000:
            # Insert 10000 rows in database
            insert.insert_node_list(self.nodelist)
            # empty the list of nodes
            self.nodelist.clear()
           
#        print('IDnode: ', n.id
#              , ' - Version: ', n.version
#              , ' - Timestamp: ', n.timestamp
#              , ' - Visible:' , n.visible 
#              , ' - UID: ' , n.uid
#              , ' - User: ', n.user
#              , ' - ChangesetID: ' , n.changeset
#              , ' - Location: ', n.location
#              , ' - Tags: ', n.tags)
#        print("\n")

    def empty_nodelist(self):
        print("Empty node list")
        if len(self.nodelist) > 0 :
            insert.insert_node_list(self.nodelist)
    
    def way(self, w):
        idway = str(w.id)+str(w.version)
        taghstore = ""
        for t in w.tags:
            taghstore += "\""+t.k.replace('\\', '\\\\').replace('"','\\"')+"\"=>\""+t.v.replace('\\', '\\\\').replace('"','\\"')+"\","
        taghstore = taghstore[:-1] # remove the last comma
        
        if len(w.nodes) == 0 :
            composedof = "{}"
        else:
            composedof = "{"
            for n in w.nodes:
                composedof += str(n.ref)+","
            composedof = composedof[:-1] # Remove last comma
            composedof += "}"
        
        self.waylist.append((idway, w.id, w.version, w.changeset, w.uid,
                            w.user.replace('\\', '\\\\').replace('"','\\"'),
                            w.timestamp, taghstore, w.visible, composedof))
        if len(self.waylist) == 10000:
            # Insert 10000 rows in database
            insert.insert_way_list(self.waylist)
            # empty the list of nodes
            self.waylist.clear()
            
    def empty_waylist(self):
        print("Empty way list")
        if len(self.waylist) > 0 :
            insert.insert_way_list(self.waylist)

    def relation(self, r):
        idrel = str(r.id)+str(r.version)
        taghstore = ""
        if len(r.tags) >0 :
            for t in r.tags:
                taghstore += "\""+t.k.replace('\\', '\\\\').replace('"','\\"')+"\"=>\""+t.v.replace('\\', '\\\\').replace('"','\\"')+"\","
            taghstore = taghstore[:-1] # remove the last comma
        
        
        self.relationlist.append((idrel, r.id, r.version, r.changeset, r.uid,
                            r.user.replace('\\', '\\\\').replace('"','\\"'),
                            r.timestamp, taghstore, r.visible))
        if len(self.relationlist) >= 10000:
            # Insert 10000 rows in database
            insert.insert_relation_list(self.relationlist)
            # empty the list of nodes
            self.relationlist.clear()
        
        if len(r.members) > 0:
            for mb in r.members:
                self.relationmblist.append((idrel, mb.ref, str(mb.type), str(mb.role)))
#                print('Type: ', mb.type,
#                      '- Ref: ', mb.ref,
#                      '- Role: ', mb.role)
       
        if len(self.relationlist) >= 10000:
            insert.insert_relation_list(self.relationlist)
            self.relationmblist.clear()
        if len(self.relationmblist) >= 10000:
            insert.insert_relationmb_list(self.relationmblist)
            self.relationmblist.clear()
                    

    def empty_relationlist(self):
        print("Empty relation list")
        # Insert the remaining relations
        if len(self.relationlist)>0:
            insert.insert_relation_list(self.relationlist)
            self.relationlist.clear
        # Insert the remaining relation members
        if len(self.relationmblist)>0:
            insert.insert_relationmb_list(self.relationmblist)
            self.relationmblist.clear()
        

tdeb = datetime.now()
print(tdeb)
tlhandler = TimelineHandler()
tlhandler.apply_file("D:/Users/qttruong/data/ile-de-france.osh.pbf")
tlhandler.empty_nodelist()
print("All nodes imported")
tlhandler.empty_waylist()
print("All ways imported")
tlhandler.empty_relationlist()
print("All relations imported")

tfin = datetime.now()
print('début: ', tdeb, ' - fin: ', tfin, ' - durée totale : ', tfin-tdeb)
