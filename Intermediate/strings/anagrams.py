def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage:
print(are_anagrams("listen", "silent"))  # Output: True
