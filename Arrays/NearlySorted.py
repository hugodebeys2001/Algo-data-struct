#https://www.geeksforgeeks.org/problems/nearly-sorted-1587115620/1

import heapq

class Solution:

    # Fonction pour retourner le tableau trié.
    def nearlySorted(self, a, n, k):
        # Créer un min-heap vide
        min_heap = []
        # Initialiser le tableau trié vide
        sorted_array = []

        # Insérer les k+1 premiers éléments dans le min-heap
        for i in range(k + 1):
            heapq.heappush(min_heap, a[i])

        # Traiter les éléments restants
        for i in range(k + 1, n):
            # Extraire le plus petit élément du min-heap et l'ajouter au tableau trié
            sorted_array.append(heapq.heappop(min_heap))
            # Insérer le prochain élément du tableau dans le min-heap
            heapq.heappush(min_heap, a[i])

        # Extraire les éléments restants du min-heap et les ajouter au tableau trié
        while min_heap:
            sorted_array.append(heapq.heappop(min_heap))

        # Retourner le tableau trié
        return sorted_array
