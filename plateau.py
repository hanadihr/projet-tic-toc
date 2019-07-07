__authors__ = "Daghmoura Riadh - El Wardani Ammar"
__date__ = "09/12/2018"

"""
    Ce fichier represente le tableau de jeu, c'est la seule interface 
    controlant les cases du jeu, le comportement de l'ordinateur et 
    detectant la fin du jeu.
"""

from case import Case
from random import randrange, choice


class Plateau:

    """
    Classe modélisant le plateau du jeu Tic-Tac-Toe.

    Attributes:
        cases (dictionary): Dictionnaire de cases. La clé est une position (ligne, colonne),
                            et la valeur est une instance de la classe Case.
    """

    def __init__(self):
        """
        Méthode spéciale initialisant un nouveau plateau contenant les 9 cases du jeu.
        """

        # Dictionnaire de cases.
        # La clé est une position (ligne, colonne), et la valeur est une instance de la classe Case.
        self.cases = {}

        self.difficulte = None

        # Appel d'une méthode qui initialise un plateau contenant des cases vides.
        self.initialiser()

    def initialiser(self):
        """
        Méthode fournie permettant d'initialiser le plateau avec des cases vides (contenant des espaces).
        """

        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.cases.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Case.
        # dont l'attribut "contenu" serait un espace (" ").
        for i in range(0, 3):
            for j in range(0, 3):
                self.cases[i,j] = Case(" ")

    def __str__(self):
        """Méthode spéciale fournie indiquant à Python comment représenter une instance de Plateau
        sous la forme d'une chaîne de caractères. Permet donc d'afficher le plateau du jeu
        à l'écran en faisant par exemple:
        p1 = Plateau()
        print(p1)
        Donc, lorsque vous affichez un objet, Python invoque automatiquement la méthode __str__
        Voici un exemple d'affichage:
         +-0-+-1-+-2-+
        0|   | X | X |
         +---+---+---+
        1| O | O | X |
         +---+---+---+
        2|   |   | O |
         +---+---+---+

        Returns:
            string: Retourne la chaîne de caractères à afficher.
        """
        s = " +-0-+-1-+-2-+\n"
        for i in range(0, 3):
            s += str(i)+ "| "
            for j in range(0, 3):
                s += self.cases[(i,j)].contenu + " | "
            if i<=1:
                s += "\n +---+---+---+\n"
            else:
                s += "\n +---+---+---+"
        return s

    def non_plein(self):
        """
        Retourne si le plateau n'est pas encore plein.
        Il y a donc encore des cases vides (contenant des espaces et non des "X" ou des "O").

        Returns:
            bool: True si le plateau n'est pas plein, False autrement.
        """
        return any(case.est_vide() for case in self.cases.values())

    def position_valide(self, ligne, colonne):
        """
        Vérifie si une position est valide pour jouer.
        La position ne doit pas être occupée.
        Il faut utiliser la méthode est_vide() de la classe Case.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.

        Returns:
            bool: True si la position est valide, False autrement.
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."

        if ligne not in range(0,3) or colonne not in range(0,3):
            return False
        return self.cases[ligne,colonne].est_vide()

    def selectionner_case(self, ligne, colonne, pion):
        """
        Permet de modifier le contenu de la case
        qui a les coordonnées (ligne,colonne) dans le plateau du jeu
        en utilisant la valeur de la variable pion.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.
            pion (string): Une chaîne de caractères ("X" ou "O").
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        self.cases[ligne, colonne] = Case(pion)


    def est_gagnant(self, pion):
        """
        Permet de vérifier si un joueur a gagné le jeu.
        Il faut vérifier toutes les lignes, colonnes et diagonales du plateau.

        Args:
            pion (string): La forme du pion utilisé par le joueur en question ("X" ou "O").

        Returns:
            bool: True si le joueur a gagné, False autrement.
        """

        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        regles_vic = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
                      [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],
                      [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
        return any(all(self.cases[j].est_pion(pion) for j in regle) for regle in regles_vic)


    def choisir_prochaine_case(self, pion):
        """
        Permet de retourner les coordonnées (ligne, colonne) de la case que l'ordinateur
        peut choisir afin de jouer contre un autre joueur qui est normalement une personne.
        Ce choix doit se faire en fonction de la configuration actuelle du plateau.
        L'algorithme que vous allez concevoir permettant de faire jouer l'ordinateur
        n'a pas besoin d'être optimal. Cela permettra à l'adversaire de gagner de temps en temps.
        Il faut par contre essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'adversaire pour que ce dernier ne gagne pas facilement.
        Il faut aussi essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'ordinateur pour que ce dernier puisse gagner.
        Vous pouvez utiliser ici la fonction randrange() du module random.
        Par exemple: randrange(1,10) vous retourne une valeur entre 1 et 9 au hasard.

        Args:
            pion (string): La forme du pion de l'adversaire de l'ordinateur ("X" ou "O").

        Returns:
            (int,int): Une paire d'entiers représentant les coordonnées de la case choisie.
        """
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        # Choix du bot qui va jouer avec la difficulté choisie au debut
        if (self.difficulte==2):
            bot = MinMaxBot()
            return bot.play(self.cases, pion)
        # Choisir une case au hasard
        test=False
        while(not test):
            ligne= randrange(0,3)
            column= randrange(0,3)
            if(self.position_valide(ligne,column)):
                test=True
        # Tester si le bot peut gagner ou empecher l'adversaire de gagner
        for x in range(0,2) :
                liste_vic_line =[[' ',pion,pion],[pion,' ',pion],[pion,pion,' ']]
                for i in range(0,3):
                # Verifier les lignes
                    for k,l in enumerate(liste_vic_line) :
                       test = True
                       for j in range(0,3) :
                           if(l[j] != self.cases[i,j].contenu):
                               test=False
                       if test:
                            return i,k
                test=True
                # Verifier les colonnes
                for i in range(0,3):

                    for k,l in enumerate(liste_vic_line) :
                        test = True
                        for j in range(0,3) :
                            if(l[j]!=self.cases[j,i].contenu):
                                test=False
                        if test:
                            return k,i
                test=True
                # Verifier la diagonale gauche
                for k,l in enumerate(liste_vic_line):
                    test = True
                    for j in range(0,3) :

                        if(l[j]!=self.cases[j,j].contenu):
                            test=False
                    if test:
                        return k,k
                test=True
                # Verifier la diagonale droite
                for k,l in enumerate(liste_vic_line):
                    test = True
                    for j in range(0,3) :
                        if(l[j]!=self.cases[j,2-j].contenu):
                            test=False
                    if test:
                        return k,2-k
                test = True
                pion = 'X' if pion=='O' else 'O'

        return(ligne,column)


# class helpers ( supposé etre dans un autre fichier mais c'est contre les règles)


X = 'X'
O = 'O'
Vide = ' '

regles_vic_convertie = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

conversion_plateau_index = {0:(0, 0), 1:(0, 1), 2:(0, 2), 3:(1, 0), 4:(1, 1), 5:(1, 2), 6:(2, 0), 7:(2, 1), 8:(2, 2)}

conversion_plateau_index2 = {(0, 0):0, (0, 1):1, (0, 2):2, (1, 0):3, (1, 1):4, (1, 2):5, (2, 0):6, (2, 1):7, (2, 2):8}

def get_contre(car):
    if car is X: return O
    return X


def get_coups_possibles(plat):
    a=[Item for Item, Value in enumerate(plat) if Value is Vide]
    return a

def conversion_plateau(plat):
    newPlat = []
    for i in range(0, 3):
        for j in range(0, 3):
            newPlat.append(plat[i, j].contenu)
    return newPlat

class MinMaxBot:
    def __init__(self):
        self.plateau = None
        self.pion = None
        self.adversaire = None
        self.jeu_finie = False
        self.base_score = None

    def play(self, Plat, Pion):
        # reinitialize this turn properties
        self.plateau = conversion_plateau(Plat)
        self.pion = Pion
        self.adversaire = get_contre(Pion)
        valeur_min = -9999
        meilleurs_coups = []
        self.base_score = len(get_coups_possibles(self.plateau))
        if self.base_score is 9:
            return conversion_plateau_index[4]
        for coup in get_coups_possibles(self.plateau):
            self.select_case(coup, Pion)
            valeur_coup = self.meilleur_coup(get_contre(Pion), -(self.base_score + 1), self.base_score + 1, 0)
            self.select_case(coup, Vide)
            if valeur_coup > valeur_min:
                valeur_min = valeur_coup
                meilleurs_coups = [coup]
            elif valeur_coup == valeur_min:
                meilleurs_coups.append(coup)
        return conversion_plateau_index[choice(meilleurs_coups)]

    def a_gagne(self):
        for pion in ('X', 'O'):
            Moves = [Move for Move, Value in enumerate(self.plateau) if Value == pion]
            for WinningState in regles_vic_convertie:
                winner = True
                for Move in WinningState:
                    if Move not in Moves:
                        winner = False
                if winner:
                    if pion is self.pion:
                        self.jeu_finie = True
                        return self.pion
                    elif pion is self.adversaire:
                        self.jeu_finie = True
                        return self.adversaire
        Items = len([Item for Item, Value in enumerate(self.plateau) if Value != Vide])
        if Items is 9:
            self.jeu_finie = True
            return 'Draw'
        return None


    def select_case(self, position, pion):
        self.plateau[position] = pion

    def meilleur_coup(self, pion, borne_inf, borne_sup, profondeur=0):
        gagnant = self.a_gagne()
        if self.jeu_finie:
            if gagnant is self.pion:
                return self.base_score - profondeur
            elif gagnant is self.adversaire:
                return profondeur - self.base_score
            elif gagnant is 'Draw':
                return 0
        for coup in get_coups_possibles(self.plateau):
            self.select_case(coup, pion)
            valeur_coup = self.meilleur_coup(get_contre(pion), borne_inf, borne_sup, profondeur + 1)
            self.select_case(coup, Vide)
            if pion == self.pion:
                if valeur_coup > borne_inf:
                    borne_inf = valeur_coup
                if borne_inf >= borne_sup:
                    return borne_sup
            else:
                if valeur_coup < borne_sup:
                    borne_sup = valeur_coup
                if borne_sup <= borne_inf:
                    return borne_inf
        if pion == self.pion:
            return borne_inf
        else:
            return borne_sup

















