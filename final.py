from elasticsearch import Elasticsearch
import itertools
import query
import querymaladie
import pymysql.cursors as pc



es = Elasticsearch()


def syno(effectList):
    liste = []
    for effect in effectList:
        b = [effect]
        result = []
        res = es.search(index='syn',body={"query":{'term':{'symptoms':effect}}})
        for hit in res['hits']['hits']:
            a=hit["_source"].get('symptoms')
            b = list(set(a).union(b))
        liste.append(b)
    return liste

def combinationsEffects(symptoms):



  a = list(itertools.product(*symptoms))


  return a

def recherche(liste):
    a = combinationsEffects(syno(liste))
    c =[]
    e = []
    for elmt in a :
        print(elmt)
        elmt = list(elmt)


        b = query.side_effect(elmt)
        d = querymaladie.disease(elmt)
        e =list(set(e).union(c))
        c =list(set(c).union(b))
    f = querymaladie.care(e)
    return(c,f)
