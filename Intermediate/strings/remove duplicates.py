def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

# Example usage:
print(remove_duplicates("banana"))  # Output: "ban"
