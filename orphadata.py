import couchdb
from elasticsearch import Elasticsearch
import time

#ATTENTION BIEN METTRE LE VPN

es = Elasticsearch()
SERVER = 'http://couchdb.telecomnancy.univ-lorraine.fr'
DB_NAME = 'orphadatabase'
couchserver = couchdb.Server(SERVER)
mydb = couchserver[DB_NAME]




INDEX_NAME = "orphadata"

if (es.indices.exists(INDEX_NAME)):
    print("deleting '%s' index..." %(INDEX_NAME))
    res = es.indices.delete(index = INDEX_NAME)
    print(" response: '%s'" % (res))

request_body = {
    "settings" : {
        "number_of_shards" : 1,
        "number_of_replicas" : 0
    }
}

print("creating '%s' index..."%(INDEX_NAME))
res=es.indices.create(index=INDEX_NAME,body=request_body)
print("creatingResponse : '%s'"%(res))
count = 1
start = time.time()
disease = ""
symptoms = []
for elt in mydb.view("clinicalsigns/GetDiseaseClinicalSignsNoLang"):
    value = elt.value
    currentDisease = value["disease"]["Name"]["text"]
    currentSymptom = value["clinicalSign"]["Name"]["text"]
    if(disease == currentDisease):
        symptoms.append(currentSymptom)
    elif(disease == ""):
        disease = currentDisease
        symptoms.append(currentSymptom)
    else :

        doc = {
                'ORPHAdisease' : disease,
                'ORPHAsymtpoms' : symptoms,
        }
        print("diseas :")
        print(disease)
        print("symptom :")
        print(symptoms)
        res = es.index(index=INDEX_NAME,doc_type='orpha',id=count,body=doc)
        count+=1
        print("fillingResponse: '%s'" % (res))
        disease = currentDisease
        symptoms[:] = []
        symptoms.append(currentSymptom)
stop = time.time()
print(stop-start)
#129.59s
