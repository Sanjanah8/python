def longest_word(sentence):
    return max(sentence.split(), key=len)

# Example usage:
print(longest_word("Find the longest word in this sentence"))  # Output: "sentence"
