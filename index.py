from lxml import etree

from elasticsearch import Elasticsearch

es = Elasticsearch()

INDEX_NAME = 'drugbank'
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


tree = etree.parse("sources/drugbank.xml")
root = tree.getroot()
a=1
for child in root.findall('drug'):
    # doc = {
    # 'toxicity': str(child.find('toxicity').text) ,
    # 'care' : str(child.find('indication').text),
    # 'name' : str(child.find('name').text)
    # }
    # res = es.index(index=INDEX_NAME,doc_type='medicament',id=a,body=doc)
    # a=a+1
    print("toxicity : '%s'" %(str(child.find('toxicity').text)))
    print("care : '%s'" %(str(child.find('indication').text)))
    print("name : '%s'" %(str(child.find('name').text)))
    #print("response: '%s'" % (res))
