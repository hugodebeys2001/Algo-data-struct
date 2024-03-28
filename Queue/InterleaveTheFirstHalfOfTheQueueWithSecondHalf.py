from typing import List


class Solution:
    def rearrangeQueue(self, N: int, q: List[int]) -> List[int]:
        liste = []
        a = 0
        long = len(q)//2
        for value in q:
            liste.append(value)
            b = min(N - 1, (N // 2) + a)  # Assure que b ne dépasse pas N - 1
            liste.append(q[b])
            a += 1
            if a >= long:
                break
        return liste