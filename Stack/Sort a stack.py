class Solution:
    def Sorted(self, stack):
        aux_stack = []

        while stack:
            temp = stack.pop()
            # Move elements from the auxiliary stack to the main stack until
            # the top of the auxiliary stack is greater than the current element
            while aux_stack and aux_stack[-1] < temp:
                stack.append(aux_stack.pop())

            # Push the current element to the auxiliary stack
            aux_stack.append(temp)

        # At this point, the auxiliary stack contains the sorted elements
        # Pop elements from the auxiliary stack to the main stack
        while aux_stack:
            stack.append(aux_stack.pop())