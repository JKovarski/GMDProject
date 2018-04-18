import networkx
import obonet
import re

path = 'C:/Users/Julien/Desktop/GMD/hp.obo'
graph = obonet.read_obo(path)


synonym=graph.nodes(data='synonym')
name=graph.nodes(data='name')
xref=graph.nodes(data='xref')

id = [id_ for id_ in graph.nodes(data=True)] #liste qui contient les id

#on a quelque chose de la forme [[XREF 1, XREF2], [NOM, SYNONYME1, SYNONYME2]] avec XREF = C1859516 par ex
#on ressort quelque chose de la forme [ID [ NOM, SYNONYME1, SYNONYM2]]
t=[] #on initialise
l=[]
l2=[]
for i in range(len(id)): #on pourrait etre plus opti mais jy arrive pas
    t.append(id[i][0])# on recupere les id dans t
for elt in t: #on parcourt la liste des id
    if xref[elt] is not None : #on parse xref si il nest pas nul
        parsedXref=[]
        for ref in xref[elt]:
            if(re.findall("UMLS:",ref)):
                parsedXref.append(ref.split(":")[1])
    if synonym[elt] is not None : #on parse synonyme si il nest pas nul
        parsedSyn=[]
        for syn in synonym[elt]:
            parsedSyn.append(syn.split("\"")[1])
        l2.append([parsedXref, [name[elt]] + parsedSyn])
        l.append([elt, [name[elt]] + parsedSyn])
    else :
        l2.append([parsedXref, name[elt]])
        l.append([elt, name[elt]])


def getIDFromSymptom(symptom) :
    listHP = []
    for i in range(len(l)) :
        for j in range (len(l[i][1])) :
            if re.findall(symptom, l[i][1][j],flags=re.IGNORECASE) :
                if l[i][0] not in listHP :
                    listHP.append(l[i][0])
    return listHP
#Exemple :
#getIDFromSymptom("Malformation of the mandible")
#getIDFromSymptom("cancer")

def getUMLSFromSymptom(symptom) :
    listUMLS = []
    for i in range(len(l2)):
        for j in range(len(l2[i][1])):
            if re.findall(symptom, l2[i][1][j], flags=re.IGNORECASE):
                for UMLS in l2[i][0]:
                    if UMLS not in listUMLS :
                        listUMLS.append(UMLS)
                #listUMLS.append(l2[i][0])
    return listUMLS
#getUMLSFromSymptom("cancer")