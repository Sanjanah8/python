from collections import Counter

def char_frequency(s):
    return dict(Counter(s))

# Example usage:
print(char_frequency("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
