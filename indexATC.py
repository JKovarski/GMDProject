
from elasticsearch import Elasticsearch

es = Elasticsearch()

INDEX_NAME = 'atcstitch'
# create ES client, create index
if es.indices.exists(INDEX_NAME):
    print("deleting '%s' index..." % (INDEX_NAME))
    res = es.indices.delete(index = INDEX_NAME)
    print(" response: '%s'" % (res))
# since we are running locally, use one shard and no replicas
request_body = {
    "settings" : {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
}
print("creating '%s' index..." % (INDEX_NAME))
res = es.indices.create(index = INDEX_NAME, body = request_body)
print(" response: '%s'" % (res))

with open('atc.txt') as f:
    count=1
    for line in f:
        a,b=line.split(' ',1)

        doc = {
        'ATC': a,
        'name':b,
        'CIDs':'0',
        'CIDm':'0',
        }
        res = es.index(index=INDEX_NAME,doc_type= 'ATC_stich' ,id=count,body=doc)
        count+=1
        print(" response: '%s'" % (res))

with open('stitch.tsv') as f:
    for line in f:
        a,b,c,d=line.split(' ',3)
        res= es.search(index=INDEX_NAME,body={"query":{'match':{'ATC':d}}})
        for hit in res['hits']['hits']:
            id=hit["_id"]
        changement = {
        'doc':{'CIDs':b,'CIDm':a}
        }
        res = es.update(index=INDEX_NAME,doc_type='ATC_stich',id=id,
                body=changement)
