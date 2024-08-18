def min_difference_pair(lst):
    lst = sorted(lst)
    min_diff = float('inf')
    pair = (None, None)
    for i in range(len(lst) - 1):
        diff = lst[i+1] - lst[i]
        if diff < min_diff:
            min_diff = diff
            pair = (lst[i], lst[i+1])
    return pair

# Example usage:
print(min_difference_pair([1, 3, 6, 9, 15]))  # Output: (6, 9)
