def caesar_cipher(s, shift):
    result = []
    for char in s:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result.append(chr(start + (ord(char) - start + shift) % 26))
        else:
            result.append(char)
    return ''.join(result)

# Example usage:
print(caesar_cipher("abc xyz", 3))  # Output: "def abc"
