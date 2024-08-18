def contains_sublist(lst, sublist):
    return any(sublist == lst[i:i+len(sublist)] for i in range(len(lst) - len(sublist) + 1))

# Example usage:
print(contains_sublist([1, 2, 3, 4, 5], [2, 3]))  # Output: True
