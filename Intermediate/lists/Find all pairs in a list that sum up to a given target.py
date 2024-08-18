def find_pairs(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

# Example usage:
print(find_pairs([1, 2, 3, 4, 5], 6))  # Output: [(1, 5), (2, 4)]
