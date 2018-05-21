from tkinter import*

def rech():
	#Mettre ici l'ensemble des actions à effectuer lors de la recherche
	print("OK");

def add(nb):
	nb += 1
	"var_saisie"+str(nb) = StringVar()
	"symptom"+str(nb) =Entry(fenetre, textvariable="var_saisie"+str(nb), width=30)	
	"symptom"+str(nb).pack();
	print("symptom"+str(nb))

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
bouton_ajout = Button(fenetre, text="Add symptom", command=add(nb_symptoms))
#bouton quitter
bouton_quitter =Button(fenetre, text="Quitter", command=fenetre.quit)



#Affichage des éléments 
titre_label.pack()
ligne_saisie.pack()
bouton_recherche.pack()
bouton_ajout.pack()
bouton_quitter.pack()




fenetre.mainloop()

