def guess_the_word():
    word = "python"
    guessed_word = ["_"] * len(word)
    attempts = 6

    while attempts > 0 and "_" in guessed_word:
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

        print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word.")
    else:
        print(f"Game over! The word was: {word}")

guess_the_word()
