from tkinter import*

def rech():
	#Mettre ici l'ensemble des actions à effectuer lors de la recherche
	print("OK");


#Création fenêtre 
fenetre = Tk()
fenetre.title("Système d'agrégation de données médicales")
fenetre.geometry("600x400")
nb_symptoms = 1

#Titre 
titre_label = Label(fenetre, text="Indiquez les symptômes :")


#Zone de saisie
var_saisie = StringVar()
ligne_saisie = Entry(fenetre, textvariable=var_saisie, width=30)

#Bouton de recherche
bouton_recherche = Button(fenetre, text="Rechercher", command=rech)

#Bouton pour ajouter symptome
bouton_ajout = Button(fenetre, text="Add symptom")
#bouton quitter
bouton_quitter =Button(fenetre, text="Quitter", command=fenetre.quit)

background_image=PhotoImage("pictures\\rouge.png")
background_label = Label(fenetre, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = background_image

#Affichage des éléments 
background_label.pack()
titre_label.pack()
ligne_saisie.pack()
bouton_recherche.pack()
bouton_ajout.pack()
bouton_quitter.pack()




fenetre.mainloop()

