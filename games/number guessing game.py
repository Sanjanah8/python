import random

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

number_guessing_game()
