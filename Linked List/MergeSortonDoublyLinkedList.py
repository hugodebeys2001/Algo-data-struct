#https://www.geeksforgeeks.org/problems/merge-sort-on-doubly-linked-list/1
# Fonction pour fusionner deux moitiés de la liste.
def merge(first, second):
    # Cas de base où l'une des deux moitiés est nulle.
    if first is None:
        return second
    if second is None:
        return first

        # Comparaison des données dans les deux moitiés et stockage du plus petit dans le résultat.
    # Appel récursif de la fonction de fusion pour le nœud suivant dans le résultat.
    if first.data < second.data:
        first.next = merge(first.next, second)
        first.next.prev = first
        first.prev = None
        # Retourne la liste résultante.
        return first
    else:
        second.next = merge(first, second.next)
        second.next.prev = second
        second.prev = None
        # Retourne la liste résultante.
        return second

    # Fonction pour trier la liste doublement chaînée donnée en utilisant le tri par fusion.


def sortDoubly(head):
    if head is None:
        return head
    if head.next is None:
        return head

        # Division de la liste en deux moitiés.
    second = split(head)

    # Appel récursif de la fonction sortDoubly pour chaque moitié séparément.
    head = sortDoubly(head)
    second = sortDoubly(second)

    # Appel de la fonction pour fusionner les deux moitiés.
    return merge(head, second)


# Fonction pour diviser la liste en deux moitiés.
def split(head):
    # Utilisation de deux pointeurs pour trouver le point milieu de la liste.
    fast = slow = head

    # Le premier pointeur (slow) avance d'un nœud et le second pointeur (fast) avance
    # de deux nœuds à chaque itération.
    while (True):
        if fast.next is None:
            break
        if fast.next.next is None:
            break
        fast = fast.next.next
        slow = slow.next

    # slow est avant le milieu de la liste, donc on divise la liste en deux moitiés à partir de ce point.
    temp = slow.next
    slow.next = None
    return temp
