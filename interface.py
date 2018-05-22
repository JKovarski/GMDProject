from PIL import ImageTk,Image
try:
    # for Python2
    import Tkinter as tk  ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    import tkinter as tk   ## notice lowercase 't' in tkinter here


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
        


        #Placement des composants
        order.place(in_=self, x=150, y=150, width=300, height=30)
        line.place(in_=self, x=150, y=200, width=300, height=30)
        order2.place(in_=self, x=100, y=250,width=400, height=30)
        search_button.place(in_=self, x=470, y=200, width=70, height=30)
        quit_button.place(in_=self,x=500, y=350, width=70, height=30)
        title.pack()
    
    def Search(self, symptoms):
        
        liste = symptoms.split(";")

        for s in liste:
            print(s)
            #Effectuer les actions de recherche ici

        test = tk.Label(self, text=liste[0], font=("Arial", 15))
        test.place(in_=self, x=100, y=380,width=400, height=30)
        
app = MainView()
app.title("Medical data aggregation system")
app.wm_geometry("600x500")
app.mainloop()
