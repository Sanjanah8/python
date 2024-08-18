def all_substrings(s):
    substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    return substrings

# Example usage:
print(all_substrings("abc"))  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
