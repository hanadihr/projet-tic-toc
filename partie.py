__authors__ = "Daghmoura Riadh - El Wardani Ammar"
__date__ = "09/12/2018"

"""
    Ce fichier permet de controler la partie de jeu en commencant 
    par demander les informations nécessaires pour jouer, alterner 
    les tours des joueurs, demander a la classe plateau si le jeu est terminé,
    afficher le jeu et de recommencer si l'utilisateur l'a demandé
"""
from plateau import Plateau
from joueur import Joueur


import os
from itertools import cycle


class Partie:
    """
    Classe modélisant une partie du jeu Tic-Tac-Toe utilisant
    un plateau et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        plateau (Plateau): Le plateau du jeu contenant les 9 cases.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None)
        nb_parties_nulles (int): Le nombre de parties nulles (aucun joueur n'a gagné).
    """

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Tic-Tac-Toe.
        """
        self.plateau = Plateau()    # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []       # La liste des deux joueurs (initialement une liste vide).
                                # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
                                    # Pendant le jeu et à chaque tour d'un joueur,
                                    # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def jouer(self):

        """
        Permet de démarrer la partie en commençant par l'affichage de ce texte:

        Bienvenue au jeu Tic Tac Toe.
        ---------------Menu---------------
        1- Jouer avec l'ordinateur.
        2- Jouter avec une autre personne.
        0- Quitter.
        -----------------------------------
        Entrez s.v.p. un nombre entre 0 et 2:?

        Cette méthode doit donc utiliser la méthode saisir_nombre().
        Elle doit par la suite demander à l'utilisateur les noms des joueurs.
        Veuillez utiliser 'Colosse' comme nom pour l'ordinateur.
        Il faut créer des instances de la classe Joueur et les ajouter à la liste joueurs.
        Il faut utiliser entre autres ces méthodes:
            *- demander_forme_pion(): pour demander au premier joueur la forme de son pion (X ou O).
              (Pas besoin de demander à l'autre joueur ou à l'ordinateur cela, car on peut le déduire).
            *- plateau.non_plein(): afin d'arrêter le jeu si le plateau est plein (partie nulle).
            *- tour(): afin d'exécuter le tour du joueur courant.
            *- plateau.est_gagnant(): afin de savoir si un joueur a gagné et donc arrêter le jeu.
        Il faut alterner entre le premier joueur et le deuxième joueur à chaque appel de tour()
        en utilisant l'attribut joueur_courant.
        Après la fin de chaque partie, il faut afficher les statistiques sur le jeu.
        Voici un exemple:

        Partie terminée! Le joueur gagnant est: Colosse
        Parties gagnées par Mondher : 2
        Parties gagnées par Colosse : 1
        Parties nulles: 1
        Voulez-vous recommencer (O,N)?

        Il ne faut pas oublier d'initialiser le plateau avant de recommencer le jeu.
        Si l'utilisateur ne veut plus recommencer, il faut afficher ce message:
        ***Merci et au revoir !***
        """


        # Affichage menu principal
        print('---------------Menu---------------')
        print("1- Jouer avec l'ordinateur.")
        print("2- Jouter avec une autre personne.")
        print("0- Quitter.")
        rep = self.saisir_nombre(0, 2)
        if rep==0:
            print("*** Merci et au revoir ! ***")
            return
        # Entrée des informations sur les joueurs
        type = 'Personne'
        for i in range(0, rep):
            print("Entrez s.v.p votre nom:? ")
            name = input()
            if i==1:
                break
            playerPion = self.demander_forme_pion()
            self.joueurs.append(Joueur(name, type, playerPion))
        if rep==1:
            # Choix de la difficulté
            print('---------------Difficulté---------------')
            print("1- Normal.")
            print("2- Imbattable.")
            self.plateau.difficulte = self.saisir_nombre(1,2)
            name = 'Colosse'
            type = 'Ordinateur'
        # Initialisation des données de joueurs
        playerPion = 'X' if playerPion == 'O' else 'O'
        self.joueurs.append(Joueur(name, type, playerPion))
        a_gagne = -1
        alternateur = cycle([0,1])
        self.joueur_courant = next(alternateur)
        rejouer = 1
        if rep in [1, 2]:
            while(rejouer==1):
                while (True):
                    # Jouer les tours des joueurs
                    if(self.joueurs[self.joueur_courant].type == 'Personne') :
                        self.tour(2)
                    else :
                        self.tour(rep)
                    # Detection d'un gagnant
                    for i in range(0,2):
                        if self.plateau.est_gagnant(self.joueurs[i].pion):
                            a_gagne= i
                            break
                    # Detection d'une partie nulle
                    if not (self.plateau.non_plein()) and a_gagne == -1:
                        a_gagne=2
                    if a_gagne!=-1:
                        break
                    # Alterner le tour
                    self.joueur_courant = next(alternateur)

                self.clean_print_plateau("Jeu Termine\n")
                if a_gagne!=2:
                    self.joueurs[a_gagne].gagne()
                    print("\n\n"+self.joueurs[a_gagne].nom +" ("+self.joueurs[a_gagne].pion+ ") A Gagne")
                else:
                    print("\n\nPartie nulle")
                    self.nb_parties_nulles+=1
                # Affichage des statistiques
                print("\n"+ "Partie gagne par "+self.joueurs[0].nom+": "+str(self.joueurs[0].nb_parties_gagnees))
                print("Partie gagne par " + self.joueurs[1].nom + ": " + str(self.joueurs[1].nb_parties_gagnees))
                print("Partie nulle: " +str(self.nb_parties_nulles))
                # Recommencer ??
                print("\nVoulez vous recommencer? (0 (non),1 (oui))")
                rejouer = self.saisir_nombre(0,1)
                if rejouer==1:
                    # Reinitialsation pour recommencer
                    difficulte = self.plateau.difficulte
                    self.plateau = Plateau()
                    self.plateau.difficulte = difficulte
                    alternateur = cycle([0, 1])
                    self.joueur_courant = next(alternateur)
                    a_gagne=-1

        print("*** Merci et au revoir ! ***")

    def clean_print_plateau(self,str):
        clear_screen()
        print(str)
        print(self.plateau)

    def saisir_nombre(self, nb_min, nb_max):
        """
        Permet de demander à l'utilisateur un nombre et doit le valider.
        Ce nombre doit être une valeur entre nb_min et nb_max.
        Vous devez utiliser la méthode isnumeric() afin de vous assurer que l'utilisateur entre
        une valeur numérique et non pas une chaîne de caractères.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Args:
            nb_min (int): Un entier représentant le minimum du nombre à entrer.
            nb_max (int): Un entier représentant le maximum du nombre à entrer.

        Returns:
            int: Le nombre saisi par l'utilisateur après validation.
        """
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."

        while(True):
            print('Entrez s.v.p un nombre entre ' + str(nb_min) +' et ' + str(nb_max) + ' : ?')
            nb=input()
            if (((nb.isnumeric()) and (int(nb)>=nb_min) and (int(nb)<=nb_max) )) :
                return (int(nb))
            else:
                print("*** Valeur incorrecte! ***")



    def demander_forme_pion(self):
        """
        Permet de demander à l'utilisateur un caractère et doit le valider.
        Ce caractère doit être soit 'O' soit 'X'.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Returns:
            string: Le catactère saisi par l'utilisateur après validation.
        """
        while (True):
            print("Sélectionnez s.v.p la forme de votre pion(X,O)")
            formePion=input()
            if(formePion in {'X','O'}):
                return formePion


    def tour(self, choix):
        """
        Permet d'exécuter le tour d'un joueur (une personne ou un ordinateur).
        Cette méthode doit afficher le plateau (voir la méthode __str__() de la classe Plateau).
        Si le joueur courant est un ordinateur, il faut calculer la position de la prochaine
        case à jouer par cet ordinateur en utilisant la méthode choisir_prochaine_case().
        Si le joueur courant est une personne, il faut lui demander la position de la prochaine
        case qu'il veut jouer en utilisant la méthode demander_postion().
        Finalement, il faut utiliser la méthode selectionner_case() pour modifier le contenu
        de la case choisie soit par l'ordinateur soit par la personne.

        Args:
            choix (int): Un entier représentant le choix de l'utilisateur dans le menu du jeu (1 ou 2).
        """

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."

        self.clean_print_plateau("Tour de "+self.joueurs[self.joueur_courant].nom +"("+self.joueurs[self.joueur_courant].pion+ ")\n\n")

        if (choix==2):
    	    case = self.demander_postion()
        else:
            case = self.plateau.choisir_prochaine_case(self.joueurs[self.joueur_courant].pion)

        self.plateau.selectionner_case(case[0],case[1],self.joueurs[self.joueur_courant].pion)


    def demander_postion(self):
        """
        Permet de demander à l'utilisateur les coordonnées de la case qu'il veut jouer.
        Cette méthode doit valider ces coordonnées (ligne,colonne).
        Voici un exemple de ce qu'il faut afficher afin de demander cette position:

        Mondher : Entrez s.v.p. les coordonnées de la case à utiliser:
        Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? 0
        Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? 0

        Il faut utiliser la méthode saisir_nombre() et position_valide().

        Returns:
            (int,int):  Une paire d'entiers représentant les
                        coordonnées (ligne, colonne) de la case choisie.
        """
        ligne = -1
        colonne = -1
        invalide = False
        while(not self.plateau.position_valide(ligne,colonne)):
            if invalide:
                print ('\nCase deja occupée')
            print('\n\nLigne: ',end='')
            ligne = self.saisir_nombre(0,2)
            print('Colonne: ',end='')
            colonne = self.saisir_nombre(0,2)
            invalide = True
        return ligne,colonne



# Permet d'effacer le contenu de la console (cross-platform)
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()
    partie.jouer()
