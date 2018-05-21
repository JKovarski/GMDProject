import os
import re
import time
from hpAnno import *
from hpObo import *
from elasticsearch import Elasticsearch



class omimClass :

    def getDiseaseNameFromOMIMID(self,omimIDListInuput):
        omimIDList = omimIDListInuput[:]
        omimIDList.sort()
        diseases = []
        my_path = os.path.abspath(os.getcwd())
        path = my_path + '/sources/omim.txt'
        file = open(path, "r")
        for line in file :
                if re.match('\*FIELD\* NO',line):
                    rawdata = next(file)
                    data = rawdata.strip()
                    if (omimIDList and omimIDList[0].split(":")[1] == data): #check if not empty
                        next(file)
                        #print(next(file).split(" ", 1)[1].strip())
                        diseases.append(next(file).split(" ", 1)[1].strip())
                        omimIDList.pop(0)
        file.close()
        return diseases


#Example
# slow so i create an index
# test = omimClass()
# test.getDiseaseNameFromOMIMID(["OMIM:203500","OMIM:208000","OMIM:614473","OMIM:156510"])

es = Elasticsearch()

INDEX_NAME = "omimtxt"
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
start = time.time()
my_path = os.path.abspath(os.getcwd())
file = my_path + '/sources/omim.txt'
newLine = " "
with open(file) as file:
    count = 1
    for line in file :
        if re.match('\*FIELD\* NO',line):
            rawdata = next(file)
            data = rawdata.strip()
            id = "OMIM:"+data
            next(file)
            diseases = next(file).split(" ", 1)[1].strip()
            #pas sur que ce soit utile
            # while not(re.match("\*FIELD\* TX",newLine)):
            #     newLine = next(file)
            #     diseases.append(newLine.strip(";\n"))
            # print(diseases)
            doc = {
                    'OMIMid' : id,
                    'OMIMdiseases' : diseases,
                }
            res = es.index(index=INDEX_NAME,doc_type='omim',id=count,body=doc)
            count+=1
            print("id :")
            print(id)
            print("diseases :")
            print(diseases)
            print("fillingResponse: '%s'" % (res))
stop = time.time()
print(stop-start)
#1129s
#18min
file.close()
