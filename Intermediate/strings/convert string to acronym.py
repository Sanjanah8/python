def to_acronym(sentence):
    return ''.join(word[0].upper() for word in sentence.split())

# Example usage:
print(to_acronym("Portable Network Graphics"))  # Output: "PNG"
