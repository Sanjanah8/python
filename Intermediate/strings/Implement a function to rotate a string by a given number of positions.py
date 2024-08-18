def rotate_string(s, n):
    n = n % len(s)
    return s[-n:] + s[:-n]

# Example usage:
print(rotate_string("abcdef", 2))  # Output: "efabcd"
