#https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1
from collections import deque

class Solution:

    # Function to find starting point where the truck can start to get through
    # the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):
        queue = deque()
        total_petrol = 0
        current_petrol = 0
        start_index = 0

        for i in range(n):
            petrol, distance = lis[i]
            queue.append((petrol, distance))
            total_petrol += petrol - distance
            current_petrol += petrol - distance

            # If current petrol becomes negative, meaning the truck can't reach the next petrol pump from the current one
            if current_petrol < 0:
                # Reset start_index to the next petrol pump
                start_index = i + 1
                current_petrol = 0
                queue.clear()  # Clear the queue since we are resetting the starting point

        # If total available petrol is non-negative, there is a solution
        # Otherwise, there is no solution
        if total_petrol >= 0:
            return start_index
        else:
            return -1
