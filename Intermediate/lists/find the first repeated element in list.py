def first_repeated(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return num
        seen.add(num)
    return None

# Example usage:
print(first_repeated([1, 2, 3, 2, 4, 5]))  # Output: 2
