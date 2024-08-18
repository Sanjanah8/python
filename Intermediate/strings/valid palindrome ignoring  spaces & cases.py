def is_valid_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Example usage:
print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # Output: True
