def max_difference(lst):
    if not lst:
        return 0
    min_val = max_val = lst[0]
    for num in lst:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
    return max_val - min_val

# Example usage:
print(max_difference([3, 10, 6, 4, 8]))  # Output: 7
