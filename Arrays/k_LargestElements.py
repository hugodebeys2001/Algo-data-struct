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

        # Le tas min contient maintenant les k plus grands éléments
        return sorted(min_heap, reverse=True)