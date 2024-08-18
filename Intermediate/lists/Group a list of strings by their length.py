from collections import defaultdict

def group_by_length(lst):
    grouped = defaultdict(list)
    for word in lst:
        grouped[len(word)].append(word)
    return dict(grouped)

# Example usage:
print(group_by_length(["a", "bb", "ccc", "dddd", "eeeee"]))  # Output: {1: ['a'], 2: ['bb'], 3: ['ccc'], 4: ['dddd'], 5: ['eeeee']}
