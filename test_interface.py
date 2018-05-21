import tkinter as tk

class PageSearch(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class PageResults(PageSearch):
   def __init__(self, *args, **kwargs):
       PageSearch.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is results page")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        ps = PageSearch(self)
        pr = PageResults(self)



        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        #BackGround    
        background_image=tk.PhotoImage("pictures\\rouge.png")
        background_label = tk.Label(container, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image
        
        #Titre
        title = tk.Label(container, text="Medical data aggregation system", font=("Arial", 25))

        #Consignes
        order = tk.Label(container, text="What are your symptoms?", font=("Arial", 12))
        order2 = tk.Label(container, text="For many symptoms, separate them with \";\"", font=("Arial", 12))
        
        #Zone de saisie
        symptoms = tk.StringVar()
        line = tk.Entry(container, textvariable=symptoms, width=50)

        #Bouton de recherche
        search_button = tk.Button(container, text="Search")
        
        #Bouton quitter
        quit_button = tk.Button(container, text="Quit", command=quit)
        


        #Placement des composants
        order.place(in_=container, x=150, y=150, width=300, height=30)
        line.place(in_=container, x=150, y=200, width=300, height=30)
        order2.place(in_=container, x=150, y=250,width=300, height=30)
        search_button.place(in_=container, x=470, y=200, width=70, height=30)
        quit_button.place(in_=container,x=500, y=350, width=70, height=30)

        title.pack()
        ps.show()

if __name__ == "__main__":
    root = tk.Tk() 

    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Medical data aggregation system")
    root.wm_geometry("600x400")
    root.mainloop()