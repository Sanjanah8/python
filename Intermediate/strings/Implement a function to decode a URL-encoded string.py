from urllib.parse import unquote

def decode_url(url):
    return unquote(url)

# Example usage:
print(decode_url("hello%20world"))  # Output: "hello world"
