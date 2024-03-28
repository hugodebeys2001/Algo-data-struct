#User function Template for python3
class Solution:
    def matchPairs(self, nuts, bolts, n):
        a = sorted(nuts)
        b = sorted(bolts)
        nuts.clear()
        bolts.clear()
        nuts.extend(a) #Ajoute les élément à la liste (qui est vide)
        bolts.extend(b)
        # J'aurais pu le faire autrement
        # Mettre des numéro à chaque symbole en fonction de son "importance"
        # Changer nuts et bolts avec des numéro et ensuite les trier