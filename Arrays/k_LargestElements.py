#https://www.geeksforgeeks.org/problems/k-largest-elements3736/1

import heapq

class Solution:
    def kLargest(self, li, n, k):
        # Créer un tas min de taille k initialisé avec les k premiers éléments
        min_heap = li[:k]
        heapq.heapify(min_heap)

        # Pour chaque élément restant dans la liste
        for num in li[k:]:
            # Si l'élément est plus grand que le plus petit élément du tas min
            if num > min_heap[0]:
                # Remplacer le plus petit élément par l'élément actuel
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        # Extraire les éléments du tas min dans l'ordre décroissant
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap))

        # Retourner les éléments dans l'ordre décroissant
        return result[::-1]
