def unique_pairs(lst, target):
    seen = set()
    pairs = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return list(pairs)

# Example usage:
print(unique_pairs([1, 2, 3, 4, 3, 2, 1], 5))  # Output: [(1, 4), (2, 3)]
