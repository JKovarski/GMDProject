import sqlite3
import os
#pourquoi from hpObo import hpOboClass() ne marche pas ?
from hpObo import *
classHP = hpOboClass()

my_path = os.path.abspath(os.getcwd())
path = my_path + '\sources\hpo_annotations.sqlite'
conn = sqlite3.connect(path)
c = conn.cursor()
#c.execute('SELECT DISTINCT  disease_db FROM phenotype_annotation')
#print(c.fetchall())

id1 = classHP.getIDFromSymptom("Malformation of the mandible")
id2 = classHP.getIDFromSymptom("headache")
t = (id1[0],)
c.execute('SELECT disease_db_and_id FROM phenotype_annotation WHERE sign_id=?', t)
out=c.fetchall()
print(out)

for id in id2 :
    t=(id,)
    c.execute('SELECT disease_db_and_id FROM phenotype_annotation WHERE sign_id=?', t)
    out = c.fetchall()
    print(out)
c.close()

def getONIM_ORPHAId(symptom):
    ONIMid= []
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
                    ONIMid.append(elt[0])
    c.close()
    return ONIMid,ORPHAid

#getONIM_ORPHAId("Malformation of the mandible")