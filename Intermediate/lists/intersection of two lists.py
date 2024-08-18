def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Example usage:
print(list_intersection([1, 2, 3], [3, 4, 5]))  # Output: [3]
