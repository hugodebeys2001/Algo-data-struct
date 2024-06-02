#https://www.geeksforgeeks.org/problems/merge-sort-on-doubly-linked-list/1
#Function to merge two halves of list.
class Node:
    def __init__(self, data):  # data -> valeur stockée dans le nœud
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    # Fonction pour fusionner deux moitiés de la liste.
    def merge(self, first, second):
        # Création d'un nœud fictif pour simplifier l'insertion initiale.
        dummy_node = Node(-1)
        ptr = dummy_node
        cur1 = first
        cur2 = second

        # Boucle tant que les deux listes ont des nœuds non traités.
        while cur1 and cur2:
            if cur1.data <= cur2.data:
                ptr.next = cur1
                cur1.prev = ptr
                cur1 = cur1.next
            else:
                ptr.next = cur2
                cur2.prev = ptr
                cur2 = cur2.next
            ptr = ptr.next

        # Attacher les nœuds restants de l'une des deux listes.
        if cur1:
            ptr.next = cur1
            cur1.prev = ptr
        if cur2:
            ptr.next = cur2
            cur2.prev = ptr

        # Le premier vrai nœud est après le nœud fictif.
        dummy_node.next.prev = None
        return dummy_node.next

    # Fonction pour trier la liste doublement chaînée donnée en utilisant le tri par fusion.
    def sortDoubly(self, head):
        if head is None:
            return head
        if head.next is None:
            return head

        # Division de la liste en deux moitiés.
        second = self.split(head)

        # Appel récursif de la fonction sortDoubly pour chaque moitié séparément.
        head = self.sortDoubly(head)
        second = self.sortDoubly(second)

        # Appel de la fonction pour fusionner les deux moitiés.
        return self.merge(head, second)

    # Fonction pour diviser la liste en deux moitiés.
    def split(self, head):
        # Utilisation de deux pointeurs pour trouver le point milieu de la liste.
        fast = slow = head

        # Le premier pointeur (slow) avance d'un nœud et le second pointeur (fast) avance
        # de deux nœuds à chaque itération.
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # slow est avant le milieu de la liste, donc on divise la liste en deux à ce point.
        temp = slow.next
        slow.next = None
        if temp:
            temp.prev = None
        return temp
