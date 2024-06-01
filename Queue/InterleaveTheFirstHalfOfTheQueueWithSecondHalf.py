#https://www.geeksforgeeks.org/problems/interleave-the-first-half-of-the-queue-with-second-half/1
from collections import deque
from typing import List


class Solution:
    def rearrangeQueue(self, N: int, q: List[int]) -> List[int]:
        # Convertir la liste en queue
        queue = deque(q)

        # Créer deux queues pour les deux moitiés
        first_half = deque()
        second_half = deque()

        # Diviser la queue initiale en deux moitiés
        for _ in range(N // 2):
            first_half.append(queue.popleft())
        for _ in range(N // 2):
            second_half.append(queue.popleft())

        # Réinitialiser la queue pour la réarranger
        result = []

        # Intercaler les éléments des deux moitiés
        while first_half and second_half:
            result.append(first_half.popleft())
            result.append(second_half.popleft())

        return result
