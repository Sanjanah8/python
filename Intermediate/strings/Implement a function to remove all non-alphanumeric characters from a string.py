def remove_non_alphanumeric(s):
    return ''.join(char for char in s if char.isalnum())

# Example usage:
print(remove_non_alphanumeric("hello, world!"))  # Output: "helloworld"
