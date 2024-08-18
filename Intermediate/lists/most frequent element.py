from collections import Counter

def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]

# Example usage:
print(most_frequent([1, 2, 3, 3, 3, 4, 4]))  # Output: 3
