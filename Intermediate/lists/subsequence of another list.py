def is_subsequence(lst1, lst2):
    it = iter(lst2)
    return all(elem in it for elem in lst1)

# Example usage:
print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))  # Output: True
