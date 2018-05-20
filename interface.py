from tkinter import*

#Création fenêtre 
fenetre = Tk()
fenetre.title("Système d'agrégation de données médicales")
fenetre.geometry("600x400")

#Titre 
titre_label = Label(fenetre, text="Indiquez les symptômes :")


#Zone de saisie
var_saisie = StringVar()
ligne_saisie = Entry(fenetre, textvariable=var_saisie, width=30)



#Bouton de recherche
bouton_recherche = Button(fenetre, text="Rechercher")


#bouton quitter
bouton_quitter =Button(fenetre, text="Quitter", command=fenetre.quit)



#Affichage des éléments 
titre_label.pack()
ligne_saisie.pack()
bouton_recherche.pack()
bouton_quitter.pack()
fenetre.mainloop()
