#https://www.geeksforgeeks.org/problems/sort-a-stack/1

class Solution:
    def Sorted(self, stack):
        # Pile auxiliaire pour stocker les éléments temporairement
        aux_stack = []

        # Tant que la pile principale n'est pas vide
        while stack:
            # Retirer le dernier élément de la pile principale
            temp = stack.pop()
            # Déplacer les éléments de la pile auxiliaire vers la pile principale
            # jusqu'à ce que le sommet de la pile auxiliaire soit plus petit que l'élément actuel
            while aux_stack and aux_stack[-1] < temp:
                stack.append(aux_stack.pop())

            # Ajouter l'élément actuel à la pile auxiliaire
            aux_stack.append(temp)
        # À ce stade, la pile auxiliaire contient les éléments triés par ordre décroissant
        # Déplacer les éléments de la pile auxiliaire vers la pile principale pour les trié par ordre croissant
        while aux_stack:
            stack.append(aux_stack.pop())
# Dans leur code, il réinverse une fois de plus la pile.
