def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

# Example usage:
sentence = "Hello World"
print(reverse_words(sentence))  # Output: "olleH dlroW"
