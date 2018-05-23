from hpAnno import *
from hpObo import *
from elasticsearch import Elasticsearch

import time
#DONT FORGET TO SETUP OMIMINDEX
hpOboClass = hpOboClass()
hpAnnoClass = hpAnnoClass()
#omimClass = omimClass()

es = Elasticsearch()

INDEX_NAME = "syn" #index name you can see it on local:9200/syn
if es.indices.exists(INDEX_NAME):
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
for elt in hpOboClass.idxrefsyn :
    OMIM,ORPHA = hpAnnoClass.getOMIM_OPHAIdFromHPId(elt[0])
    # OMIMDiseases = omimClass.getDiseaseNameFromOMIMID(OMIM)
    doc = {
        'hpID' : elt[0],
        'symptoms' : elt[1],
        'CUI' : elt[2],
        'OMIMid' : OMIM,
        'ORPHAid' : ORPHA,
        'OMIMDiseases' : '0',
    }
    print('hpID :')
    print(elt[0])
    print('symptoms :')
    print(elt[1])
    print('CUI :')
    print(elt[2])
    print('OMIM :')
    print(OMIM)
    print('ORPHA :')
    print(ORPHA)
    res = es.index(index=INDEX_NAME,doc_type='hp',id=count,body=doc)
    count+=1
    print("fillingResponse: '%s'" % (res))

stop = time.time()
print(stop - start)


# 525.3126273155212 secondes = 8.75 minutes before CUI
# 561.3911745548248 secondes after
# 702 after reboot pc
