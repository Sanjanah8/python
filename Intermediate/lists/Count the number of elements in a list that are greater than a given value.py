def count_greater_than(lst, value):
    return sum(1 for x in lst if x > value)

# Example usage:
print(count_greater_than([1, 5, 7, 3, 9], 4))  # Output: 3
