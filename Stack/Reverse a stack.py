#https://www.geeksforgeeks.org/problems/reverse-a-stack/1

from typing import List

class Solution:
    def reverse(self,St):
        liste = []
        while St:
            liste.append(St.pop())
        for j in liste:
            St.append(j)
        return St
