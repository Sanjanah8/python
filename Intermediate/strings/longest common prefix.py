def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
    return prefix

# Example usage:
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
