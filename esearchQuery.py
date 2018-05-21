from elasticsearch import Elasticsearch
import couchdb
es = Elasticsearch()

INDEX_NAME = "syn"
INDEX_NAME2 = "omimtxt"
INDEX_NAME3 = "orphadata"
symptom1 = "cervical"
symptom2 = "neck"

def getORPHAandOMIMdiseasesfromSymptom(symptom1,symptom2):
    res=es.search(index=INDEX_NAME,body={

        "query": {

            "bool": {

                "must": {

                 "wildcard": { "symptoms": symptom1 },

                },

                "must": {

                    "match": { "symptoms": symptom1}
                }

            }

        }

    })

    print("results:")

    diseases = []
    for hit in res['hits']['hits']:
        #print(hit["_source"])
        omim = hit["_source"]["OMIMid"]
        orpha = hit["_source"]["ORPHAid"]
        for omimid in omim :
            resOMIM = es.search(index=INDEX_NAME2,body={"query":{'match':{'OMIMid':omimid}}})
            for hit in resOMIM["hits"]["hits"]:
                diseases.append(hit["_source"]["OMIMdiseases"])
                # print("omim :")
                # print(hit["_source"]["OMIMid"])
                # print(hit["_source"]["OMIMdiseases"])
        for orphaid in orpha : #my index has doublons so i take only the first result
            resORPHA = es.search(index=INDEX_NAME3,body={"size":1,"query":{'match':{'ORPHAid':orphaid.split(":")[1]}}})
            for hit in resORPHA["hits"]["hits"]:
                diseases.append(hit["_source"]["diseases"])
                # print("orpha :")
                # print(hit["_source"]["ORPHAid"])
                # print(hit["_source"]["diseases"])
    return diseases
#def createQueryEsearch(listSymptom)

output = getORPHAandOMIMdiseasesfromSymptom(symptom1,symptom2)
print(output)
print(len(output))
