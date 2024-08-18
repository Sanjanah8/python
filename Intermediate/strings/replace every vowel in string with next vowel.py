def replace_vowels(s):
    vowels = 'aeiou'
    next_vowel = {vowels[i]: vowels[(i + 1) % len(vowels)] for i in range(len(vowels))}
    return ''.join(next_vowel[char] if char in next_vowel else char for char in s)

# Example usage:
print(replace_vowels("hello"))  # Output: "hillu"
