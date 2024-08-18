def common_elements(lst1, lst2, lst3):
    return list(set(lst1) & set(lst2) & set(lst3))

# Example usage:
print(common_elements([1, 2, 3], [3, 4, 5], [5, 3, 6]))  # Output: [3]
