def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

# Example usage:
print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
