
from elasticsearch import Elasticsearch
import couchdb

SERVER = 'http://couchdb.telecomnancy.univ-lorraine.fr'
DB_NAME = 'orphadatabase'
couchserver = couchdb.Server(SERVER)
mydb = couchserver[DB_NAME]

import pymysql.cursors as pc

# Connect to the database
connection = pymysql.connect(host='neptune.telecomnancy.univ-lorraine.fr',
                             user='gmd-read',
                             password='esial',
                             db='gmd')


def side_effect(side_effects):
    result1 = []
    result2 =[]
    ###### syder and ATC ###############

    with connection.cursor(pc.DictCursor) as cursor:
        liste = []
        for side in side_effects :
            medicaments=[]
            sql ="SELECT stitch_compound_id1 FROM `meddra_all_se` as "+side+" WHERE side_effect_name LIKE "+'"%'+side+'%"'+" GROUP BY stitch_compound_id1"
            cursor.execute(sql)
            for row in cursor:
                cid1 = row["stitch_compound_id1"]
                cid1 = cid1[4:]
                cid1 = 'CIDs'+cid1
                medicaments.append(cid1)
            #print(medicaments)
            liste.append(medicaments)
        final = liste[0]
        for i in range (1,len(liste)):
            final = set(liste[i]).intersection(final)
        c=0
        for cid in final :

            res =es.search(index='atcstitch',body={"query":{'match':{'CIDs':cid}}})
            for hit in res['hits']['hits']:
                a=hit["_source"].get('name').strip('\n')
                result1.append(a)

    print(len(result1))
    #################drugbank###########
    b =' '.join(side_effects)

    res =es.search(index='drugbank',body={'from':0,'size':10000,"query":{'match':{'toxicity': b }}})
    for hit in res['hits']['hits']:
            a=hit["_source"].get('name')
            result2.append(a)


    result_side = list(set(result2).union(result1))

    return (result_side)
