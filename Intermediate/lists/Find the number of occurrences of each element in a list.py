from collections import Counter

def count_occurrences(lst):
    return dict(Counter(lst))

# Example usage:
print(count_occurrences([1, 2, 2, 3, 3, 3]))  # Output: {1: 1, 2: 2, 3: 3}
