def can_form_palindrome(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    odd_count = sum(1 for count in freq.values() if count % 2 == 1)
    return odd_count <= 1

# Example usage:
print(can_form_palindrome("civic"))  # Output: True
