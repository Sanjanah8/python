def start_game():
    print("Welcome to the Adventure Game!")
    print("You are in a dark forest. There are two paths: left and right.")
    choice = input("Which path do you choose? (left/right): ").lower()

    if choice == "left":
        print("You encounter a friendly wizard who gives you a magic potion.")
        print("You win the game!")
    elif choice == "right":
        print("You encounter a wild beast and narrowly escape.")
        print("You return to the start and try again.")
        start_game()
    else:
        print("Invalid choice. Try again.")
        start_game()

start_game()
