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

class MainView(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(expand ="yes", fill ="both")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)

        #Chargement des pages
        self.frames = { }
        
        frame = StartPage(container,self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Titre
        title = tk.Label(self, text="Medical data aggregation system", font=("Arial", 22))

        #Consignes
        order = tk.Label(self, text="What are your symptoms?", font=("Arial", 12))
        order2 = tk.Label(self, text="For many symptoms, separate them with \";\"", font=("Arial", 12))
        
        #Zone de saisie
        symptoms = tk.StringVar()
        line = tk.Entry(self, textvariable=symptoms, width=50)

        #Bouton de recherche
        search_button = tk.Button(self, text="Search", command=lambda : self.Search(line.get()))

        #Bouton quitter
        quit_button = tk.Button(self, text="Quit", command=quit)
        
        #Resultats
        results = tk.Label(self, text="Results", font=("Arial", 22))

        #Placement des composants)
        order.place(in_=self, x=150, y=250, width=300, height=30)
        line.place(in_=self, x=150, y=300, width=300, height=30)
        order2.place(in_=self, x=100, y=350,width=400, height=30)
        search_button.place(in_=self, x=470, y=300, width=70, height=30)
        quit_button.place(in_=self,x=50, y=600, width=70, height=30)
        title.pack()




    def Search(self, symptoms):

        #Creation des tableaux
        tree = ttk.Treeview(self)

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
        tree.place(in_=self,x=600, y=100, width=460, height=550)
        

        tree2 = ttk.Treeview(self)
        tree2["columns"]=("one")
        tree2['show'] = 'headings' #Effacer la première colonne inutile
        tree2.column("one", width=230 )
        tree2.heading("one", text="Side effect of")
        tree2.insert("" , 0,    text="Line 1", values=("Valeur1"))
        tree2.place(in_=self,x=1110, y=100, width=230, height=550)
        
        #Recuperation des données
        if(symptoms != ""):

            listeHP = []
            listeUMLS = []
            
            liste = symptoms.split(";")

            for element in liste:
                print(element)
            
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
                    

            # test = tk.Label(self, text=liste[0], font=("Arial", 10))
            # test.pack()        
            #test.place(in_=self, x=100, y=380,width=400, height=30)
            

            for i in listeUMLS:
                print(i)



app = MainView()
app.title("Medical data aggregation system")
app.wm_geometry("1366x768")
app.mainloop()
