#https://www.geeksforgeeks.org/problems/sort-a-stack/1

class Solution:
    def trier_pile(self, pile):
        # Pile auxiliaire pour stocker les éléments temporairement
        pile_auxiliaire = []

        # Tant que la pile principale n'est pas vide
        while pile:
            # Retirer le dernier élément de la pile principale
            element_temporaire = pile.pop()

            # Déplacer les éléments de la pile auxiliaire vers la pile principale
            # jusqu'à ce que le sommet de la pile auxiliaire soit plus petit que l'élément actuel
            while pile_auxiliaire and pile_auxiliaire[-1] < element_temporaire:
                pile.append(pile_auxiliaire.pop())

            # Ajouter l'élément actuel à la pile auxiliaire
            pile_auxiliaire.append(element_temporaire)

        # À ce stade, la pile auxiliaire contient les éléments triés par ordre décroissant
        # Déplacer les éléments de la pile auxiliaire vers la pile principale pour les trié par ordre croissant
        while pile_auxiliaire:
            pile.append(pile_auxiliaire.pop())

        #Dans leur code, il réinverse une fois de plus la pile.
