def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    v_count = c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

# Example usage:
print(count_vowels_consonants("Hello World"))  # Output: (3, 7)
