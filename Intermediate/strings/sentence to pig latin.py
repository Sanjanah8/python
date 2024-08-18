def pig_latin(sentence):
    def convert_word(word):
        if word[0] in 'aeiou':
            return word + 'way'
        return word[1:] + word[0] + 'ay'

    return ' '.join(convert_word(word) for word in sentence.split())

# Example usage:
print(pig_latin("hello world"))  # Output: "ellohay orldway"
