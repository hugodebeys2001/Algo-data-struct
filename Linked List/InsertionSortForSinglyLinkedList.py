#https://www.geeksforgeeks.org/problems/insertion-sort-for-singly-linked-list/0

class Solution:
    def insertionSort(self, head):
        if not head or not head.next:
            return head  # Si la liste est vide ou ne contient qu'un seul élément, elle est déjà triée

        # Initialisation du nœud de tête de la liste triée
        sorted_head = head
        head = head.next
        sorted_head.next = None
        while head:
            current = head
            head = head.next
            current.next = None
            # Insérer le nœud courant dans la liste triée
            if current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

        return sorted_head
