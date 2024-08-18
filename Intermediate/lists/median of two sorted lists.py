def find_median_of_sorted_lists(lst1, lst2):
    merged = sorted(lst1 + lst2)
    n = len(merged)
    if n % 2 == 0:
        return (merged[n//2 - 1] + merged[n//2]) / 2
    else:
        return merged[n//2]

# Example usage:
print(find_median_of_sorted_lists([1, 3], [2]))  # Output: 2
