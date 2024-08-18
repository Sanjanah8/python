import heapq

def k_smallest_elements(lst, k):
    return heapq.nsmallest(k, lst)

# Example usage:
print(k_smallest_elements([3, 1, 4, 1, 5, 9], 3))  # Output: [1, 1, 3]
