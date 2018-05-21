import sqlite3
import os
#pourquoi from hpObo import hpOboClass() ne marche pas ?
from hpObo import *
classHP = hpOboClass()

my_path = os.path.abspath(os.getcwd())
path = my_path + '/sources/hpo_annotations.sqlite'
conn = sqlite3.connect(path)

class hpAnnoClass :

    def __init__(self,conn = conn):
        self.conn = conn

    def getOMIM_ORPHAIdFromSymptom(self,symptom):
        OMIMid= []
        ORPHAid = []
        c = conn.cursor()
        id = classHP.getIDFromSymptom(symptom)
        for differentId in id :
            t = (differentId,)
            c.execute('SELECT disease_db_and_id FROM phenotype_annotation WHERE sign_id=?', t)
            out = c.fetchall()
            for elt in out :
                if elt[0] is not None :
                    if elt[0].split(":")[0] == "ORPHA":
                        ORPHAid.append(elt[0])
                    elif elt[0].split(":")[0] == "OMIM":
                        OMIMid.append(elt[0])
        c.close()
        return OMIMid,ORPHAid
    def getOMIM_OPHAIdFromHPId(self,hpid):
        OMIMid=[]
        ORPHAid=[]
        c = conn.cursor()
        t = (hpid,)
        c.execute('SELECT disease_db_and_id FROM phenotype_annotation WHERE sign_id=?', t)
        out = c.fetchall()
        for elt in out :
            if elt[0] is not None :
                if elt[0].split(":")[0] == "ORPHA":
                    ORPHAid.append(elt[0])
                elif elt[0].split(":")[0] == "OMIM":
                    OMIMid.append(elt[0])
        c.close()
        return OMIMid,ORPHAid


# #Exemple :
hpanno = hpAnnoClass()
#print(hpanno.getOMIM_ORPHAIdFromSymptom("Malformation of the mandible"))
# print(hpanno.getOMIM_OPHAIdFromHPId("HP:0008449"))
