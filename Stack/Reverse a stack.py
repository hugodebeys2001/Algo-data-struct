from typing import List

class Solution:
    def reverse(self,St):
        liste = []
        for i in range(len(St)-1, -1, -1):
            liste.append(St[i])
        St.clear()
        for j in liste:
            St.append(j)
        return St