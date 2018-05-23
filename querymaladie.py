from elasticsearch import Elasticsearch

es = Elasticsearch()

def disease(symptoms):
    b =' '.join(symptoms)
    print(b)
    result= []
    res =es.search(index='orphadata',body={'from':0,'size':10000,"query":{'match':{'ORPHAsymtpoms': b }}})
    for hit in res['hits']['hits']:
            a=hit["_source"].get('ORPHAdisease')
            print(a)
            result.append(a)



    return result



def care(maladies):
    associate = []
    for disease in maladies:
        med = []
        res =es.search(index='drugbank',body={'from':0,'size':10000,"query":{'match':{'care': disease }}})
        for hit in res['hits']['hits']:
                a=hit["_source"].get('name')
                med.append(a)
        associate.append((disease,med))
    return associate
