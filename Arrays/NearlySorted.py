class Solution:

    # Function to return the sorted array.
    def nearlySorted(self, a, n, k):
        # Create an empty min-heap
        min_heap = []
        sorted_array = []

        # Push the first k+1 elements into the min-heap
        for i in range(k + 1):
            heapq.heappush(min_heap, a[i])

        # Process the remaining elements
        for i in range(k + 1, n):
            # Pop the smallest element from the min-heap
            sorted_array.append(heapq.heappop(min_heap))
            # Push the next element into the min-heap
            heapq.heappush(min_heap, a[i])

        # Pop the remaining elements from the min-heap
        while min_heap:
            sorted_array.append(heapq.heappop(min_heap))

        return sorted_array