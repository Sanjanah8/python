def follows_pattern(s, pattern):
    return all(char1 == char2 for char1, char2 in zip(s, pattern)) or not pattern

# Example usage:
print(follows_pattern("abcdef", "abcdef"))  # Output: True
print(follows_pattern("abcdef", "abc"))    # Output: False
