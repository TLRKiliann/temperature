#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pickle
import os

class Tempa:
	"""
	Classe des température
	"""
	jour_enplus = 0

	def __init__(self): # On ajoute des paramètres pour pouvoir les changer
		print("Création d'un jour...", self) # Affiche les adresses mémo avec "self"
		self.jour = input("Quel jour (date sous forme:../../..)? : ")
		self.nbr = input("Combien de degrés ? : ")
		Tempa.jour_enplus += 1 # Attribut de classe (variable de classe)

print("Lancement du programme...\n")
rep = input("Veux-tu commencer? o/n : ")

ch1 = "Programme de l'entreprise Esteban et Cie"
tr2 = "----------------------------------"
sharp = "####################################################"

c = 0
     
while rep != 'q':
    if rep == 'o':
        print("\nOn continue\n")
        t1 = Tempa()

        if not os.path.isfile("myfile.txt"):
            f=open("MyFichier.txt", 'at') # Append + text

            print("Jour > {}".format(t1.jour))
            print("Température > {}°".format(t1.nbr))
            print("Jours répertoriés : {}".format(t1.jour_enplus))

            f.write(str(ch1.center(50)))
            f.write(str("\n"))
            f.write(str(tr2.center(50)))
            f.write(str("\n\n"))
            f.write("Date: ")
            f.write(str(t1.jour))
            f.write(str("\n\n"))
            f.write("Température: ")
            f.write(str(t1.nbr +"C°"))
            f.write(str("\n\n"))
            f.write("N jour répertorié: ")
            f.write(str(t1.jour_enplus))
            f.write(str("\n\n"))
            f.write(str(sharp))
            f.write(str("\n\n"))
            f.close()

            rep = input("\nVeux-tu continuer? o/n : ")
            c += 1

    else: # Si on print non tout les str s'affichent !!!
        fichier = open("MyFichier.txt", 'r')
        line=fichier.readlines()
        while line:
            print(line)
            line=fichier.readlines()
        fichier.close()
        
        print("\nAu revoir!")
        break



