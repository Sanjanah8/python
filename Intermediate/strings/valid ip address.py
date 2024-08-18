import re

def is_valid_ipv4(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip))

# Example usage:
print(is_valid_ipv4("192.168.1.1"))  # Output: True
print(is_valid_ipv4("999.999.999.999"))  # Output: False
