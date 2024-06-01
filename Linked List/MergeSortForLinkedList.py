#https://www.geeksforgeeks.org/problems/sort-a-linked-list/1

class Solution:
    #Fusionne deux listes trié pour en faire une triée
    def merge_sll(self, head1, head2):
        dummy_node = Node(-1)
        ptr = dummy_node
        cur1 = head1
        cur2 = head2

        while cur1 and cur2:
            if cur1.data <= cur2.data:
                ptr.next = cur1
                cur1 = cur1.next
            else:
                ptr.next = cur2
                cur2 = cur2.next
            ptr = ptr.next

        if cur1:
            ptr.next = cur1
        if cur2:
            ptr.next = cur2
        return dummy_node.next

    def merge_sort_sll(self, head):
        if not head or not head.next:  # Base case: empty list or single node
            return head

        mid_node = head
        fast = head
        while fast and fast.next and fast.next.next:  # imp to check f.n.n fo 2 size case
            mid_node = mid_node.next
            fast = fast.next.next

        right_head = mid_node.next
        mid_node.next = None  # Break the list into two parts

        # Recursively sort both halves
        left_sorted = self.merge_sort_sll(head)
        right_sorted = self.merge_sort_sll(right_head)

        # Merge the sorted halves
        return self.merge_sll(left_sorted, right_sorted)

    def mergeSort(self, head):
        return self.merge_sort_sll(head)
