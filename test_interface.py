from PIL import ImageTk,Image
try:
    # for Python2
    import Tkinter as tk  ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    import tkinter as tk   ## notice lowercase 't' in tkinter here
import hpObo as hpo
from elasticsearch import Elasticsearch
from tkinter import ttk
from tkinter import *

es = Elasticsearch()

  
root = tk.Tk()
root.title("Medical data aggregation system")
root.wm_geometry("1366x768")

image1 = tk.PhotoImage(file="pictures/pills2.png")
w = image1.width()
h = image1.height()
root.geometry("%dx%d+0+0" % (w, h))

panel1 = tk.Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
  
#Titre
title = tk.Label(root, text="Medical data aggregation system", font=("Arial", 22))

#Consignes
order = tk.Label(root, text="What are your symptoms?", font=("Arial", 12))
order2 = tk.Label(root, text="For many symptoms, separate them with \";\"", font=("Arial", 12))
        
#Zone de saisie
symptoms = tk.StringVar()
line = tk.Entry(root, textvariable=symptoms, width=50)

#Bouton de recherche
search_button = tk.Button(root, text="Search", command=lambda : Search(line.get()))

#Bouton quitter
quit_button = tk.Button(root, text="Quit", command=quit)
        
#Resultats
results = tk.Label(root, text="Results", font=("Arial", 22))

#Placement des composants)
order.place(in_=root, x=150, y=250, width=300, height=30)
line.place(in_=root, x=150, y=300, width=300, height=30)
order2.place(in_=root, x=100, y=350,width=400, height=30)
search_button.place(in_=root, x=470, y=300, width=70, height=30)
quit_button.place(in_=root,x=50, y=600, width=70, height=30)
title.place(in_=root,x=383, y=5, width=600, height=50)




def Search(symptoms):

	#Creation des tableaux
    tree = ttk.Treeview(root)
    tree["columns"]=("one","two")
    tree.column("one", width=230 )
    tree.column("two", width=230)
    tree.heading("one", text="Potentially involved diseases")
    tree.heading("two", text="Curing drugs")
    tree['show'] = 'headings' #Effacer la première colonne inutile
    i = 0

    #Ajout d'une ligne
    while i < 100 :
    	tree.insert("" , i,    text="Line 1", values=("Valeur1","Valeur2"))
    	i = i + 1
    tree.place(in_=root,x=600, y=100, width=460, height=500)
        

    tree2 = ttk.Treeview(root)
    tree2["columns"]=("one")
    tree2['show'] = 'headings' #Effacer la première colonne inutile
    tree2.column("one", width=230 )
    tree2.heading("one", text="Side effect of")
    tree2.insert("" , 0,    text="Line 1", values=("Valeur1"))
    tree2.place(in_=root,x=1110, y=100, width=230, height=500)
        
    #Recuperation des données
    if(symptoms != ""):

        liste = symptoms.split(";")

        for element in liste:
            if (element != ""):
                print(element)
                #Effectuer ici la suite des opérations 

                    
        # for s in liste:
        #     omimlist = []    
        #     res=es.search(index="syn",body={"query":{"match":{"symptoms":s}}})
        #     for hit in res["hits"]["hits"]:
        #         print(hit["_source"]["OMIMid"])
        #         omimlist.append(hit["_source"]["OMIMid"])

        #     for s2 in omimlist:
        #         for element in s2:
        #             resOmim=es.search(index="omimtxt",body={"query":{"match":{"OMIMid":element}}})
        #             for hit in resOmim["hits"]["hits"]:
        #                 if (hit["_source"]["OMIMdiseases"] != "")(hit["_source"]["OMIMdiseases"] != "")
        #                 print(hit["_source"]["OMIMdiseases"])
                   

        # test = tk.Label(root, text=liste[0], font=("Arial", 10))
        # test.pack()        
        #test.place(in_=root, x=100, y=380,width=400, height=30)

# save the panel's image from 'garbage collection'
panel1.image = image1
  
# start the event loop
root.mainloop()