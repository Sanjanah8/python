def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome(s):
    max_len = 0
    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if is_palindrome(substr) and len(substr) > max_len:
                max_len = len(substr)
                longest = substr
    return longest

# Example usage:
print(longest_palindrome("babad"))  # Output: "bab" or "aba"
