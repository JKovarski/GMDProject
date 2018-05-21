from PIL import ImageTk,Image
try:
    # for Python2
    import Tkinter as tk  ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    import tkinter as tk   ## notice lowercase 't' in tkinter here

class PageSearch(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class PageResults(PageSearch):
   def __init__(self, *args, **kwargs):
       PageSearch.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is results page")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        ps = PageSearch(self)
        pr = PageResults(self)



        #container = tk.Frame(self)
        
        #BackGround    

        container = tk.Canvas(self, width = 200, height = 200, bg = "blue")
        container.pack(expand ="yes", fill ="both")

        image = ImageTk.PhotoImage(file = "pictures/rouge.png")
        container.create_image(100,100, image = image, anchor = "nw")

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
        

if __name__ == "__main__":
    root = tk.Tk() 
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Medical data aggregation system")
    root.wm_geometry("600x400")
    root.mainloop()