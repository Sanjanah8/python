import random

def shuffle_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def guess_the_word():
    words = ["computer", "coffee", "book", "chair", "phone", "table", "keyboard", "lamp", "television", "window"]
    attempts = 6
    word = random.choice(words)
    guessed_word = ["_"] * len(word)

    print("Welcome to the Guess the Word game!")
    
    while attempts > 0:
        scrambled_word = shuffle_word(word)
        print(f"Scrambled word: {scrambled_word}")
        print("Current guess: " + " ".join(guessed_word))
        
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        # Check if the player has guessed all letters
        if "_" not in guessed_word:
            print("Congratulations! You guessed the word.")
            word = random.choice(words)  # Choose a new word
            guessed_word = ["_"] * len(word)  # Reset the guessed word
            attempts = 6  # Reset attempts for the new word
            print(f"New word scrambled: {shuffle_word(word)}")
        else:
            print(" ".join(guessed_word))

    print(f"Game over! The word was: {word}")

guess_the_word()
