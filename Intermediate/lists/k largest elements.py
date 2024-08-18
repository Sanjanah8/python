import heapq

def k_largest_elements(lst, k):
    return heapq.nlargest(k, lst)

# Example usage:
print(k_largest_elements([1, 3, 5, 7, 9], 2))  # Output: [9, 7]
