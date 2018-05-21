import networkx
import obonet
import re
import os.path



my_path = os.path.abspath(os.getcwd())
path = my_path + '/sources/hp.obo'
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
all = []
parsedXref=[]
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
        all.append([elt,[name[elt]] + parsedSyn,parsedXref])
    else :
        l2.append([parsedXref, [name[elt]]])
        l.append([elt, [name[elt]]])
        all.append([elt,[name[elt]],parsedXref])


class hpOboClass :

    def __init__(self,ID = l, xref = l2,idxrefsyn = all):
        self.ID = ID
        self.xref = xref
        self.idxrefsyn = all

    def getIDFromSymptom(self,symptom) :
        listHP = []
        for i in range(len(l)) :
            for j in range (len(l[i][1])) :
                if re.findall(symptom, l[i][1][j],flags=re.IGNORECASE) :
                    #print(l[i][1][j])
                    if l[i][0] not in listHP :
                        listHP.append(l[i][0])
        return listHP


    def getUMLSFromSymptom(self,symptom) :
        listUMLS = []
        for i in range(len(l2)):
            for j in range(len(l2[i][1])):
                if re.findall(symptom, l2[i][1][j], flags=re.IGNORECASE):
                    for UMLS in l2[i][0]:
                        if UMLS not in listUMLS :
                            listUMLS.append(UMLS)
        return listUMLS

#Exemple :
test = hpOboClass()
# print(test.idxrefsyn)
# test.getIDFromSymptom("Malformation of the mandible")
# print(test.getIDFromSymptom("cancer"))
# print(test.getUMLSFromSymptom("cancer"))
