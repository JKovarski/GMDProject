import couchdb
import elasticsearch
import time
##ATTENTION BIEN SE CONNECTER AU VPN

SERVER = 'http://couchdb.telecomnancy.univ-lorraine.fr'
DB_NAME = 'orphadatabase'
couchserver = couchdb.Server(SERVER)
mydb = couchserver[DB_NAME]

# orphadataDict = {}
# syndromes = list()
#
# def parseOrphadata():
#     for elmt in mydb.view("clinicalsigns/GetDiseaseByClinicalSign") :
#             value = elmt.value
#             print(value)
#             clinicalSign = value["clinicalSign"]
#             clinicalSignName = clinicalSign["Name"]["text"]
#             disease = value["disease"]
#             diseaseName = disease["Name"]["text"]
#             if clinicalSignName in orphadataDict :
#                 orphadataDict[clinicalSignName].append(diseaseName)
#             else :
#                 orphadataDict[clinicalSignName] = [diseaseName]
#                 syndromes.append(clinicalSignName)
#     # il y a 49905 éléments
#
# def searchDiseaseOrphadata(self,syndrome) :
#     if(syndrome in orphadataDict):
#         return orphadataDict[syndrome]
#     else :
#         return []

#
# def getDiseaseNameFromORPHAID(orphaID):
#     for elt in mydb.view("clinicalsigns/GetDiseaseByClinicalSign") :
#         value = elt.value
#         disease=value["disease"]
#         orphaid = disease["OrphaNumber"]
#         if str(orphaid) == orphaID.split(":")[1]:
#             orphadisease = disease["Name"]["text"]
#             return orphadisease
#
# print(getDiseaseNameFromORPHAID("ORPHA:243"))


###Creationindex
es = Elasticsearch()
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
for elt in mydb.view("clinicalsigns/GetDiseaseByClinicalSign") :
    value = elt.value
    disease=value["disease"]
    orphaid = disease["OrphaNumber"]
    orphadisease = disease["Name"]["text"]

    doc = {
        'ORPHAid' : str(orphaid),
        'diseases' : orphadisease,
    }
    print('oprha id :')
    print(str(orphaid))
    print("disease :")
    print(orphadisease)
    res = es.index(index=INDEX_NAME,doc_type='orpha',id=count,body=doc)
    count+=1
    print("fillingResponse: '%s'" % (res))

stop = time.time()
print(stop-start)
#2316.770339012146s
#38min
