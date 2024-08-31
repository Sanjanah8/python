import random

def print_intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious forest with several paths ahead.")
    print("Your goal is to find the hidden treasure while managing your health and overcoming various challenges.")
    print("Good luck!")

def choose_path():
    print("\nYou come to a fork in the road.")
    print("1. Take the left path")
    print("2. Take the middle path")
    print("3. Take the right path")
    choice = input("Which path will you choose? (1/2/3): ")
    return choice

def encounter_wizard():
    print("\nYou encounter a friendly wizard.")
    print("He offers you a choice:")
    print("1. Take a magic potion")
    print("2. Take a magical sword")
    print("3. Ask for advice")
    choice = input("What do you choose? (1/2/3): ")
    if choice == "1":
        print("The potion grants you extra health.")
        return "potion"
    elif choice == "2":
        print("The sword will help you in battles.")
        return "sword"
    elif choice == "3":
        print("The wizard gives you a hint about the cave.")
        return "hint"
    else:
        print("The wizard looks disappointed and disappears.")
        return None

def encounter_beast(inventory):
    print("\nYou encounter a wild beast!")
    if "sword" in inventory:
        print("You use your sword to defeat the beast.")
        print("You continue on your journey.")
    else:
        print("You have no weapon to fight the beast.")
        print("You run away and lose some health.")
        return False
    return True

def encounter_trap(inventory):
    print("\nYou find a hidden trap!")
    if "potion" in inventory:
        print("You use the potion to escape the trap safely.")
        print("You continue on your journey.")
        inventory.remove("potion")  # Potion used
    else:
        print("You fall into the trap and lose some health.")
        return False
    return True

def encounter_random_event():
    events = [
        "You find a hidden stash of gold!",
        "You come across a wise old sage who teaches you a valuable skill.",
        "You find a map that reveals a shortcut to the treasure.",
        "You get lost and have to retrace your steps."
    ]
    print("\n" + random.choice(events))

def find_treasure():
    print("\nCongratulations! You find the hidden treasure!")
    print("You've completed the adventure successfully.")
    print("Thank you for playing!")

def main_game():
    print_intro()
    inventory = []
    health = 100
    treasure_found = False

    while True:
        print(f"\nYour health: {health}")
        path = choose_path()

        if path == "1":
            print("\nYou take the left path and come across a clearing.")
            item = encounter_wizard()
            if item:
                inventory.append(item)
            continue
        elif path == "2":
            print("\nYou take the middle path and encounter various challenges.")
            if not encounter_beast(inventory):
                health -= 20  # Losing health
                if health <= 0:
                    print("You have succumbed to your injuries. Game over.")
                    break
                continue
            if not encounter_trap(inventory):
                health -= 30  # Losing health
                if health <= 0:
                    print("You have succumbed to your injuries. Game over.")
                    break
                continue
            encounter_random_event()
            treasure_found = True
        elif path == "3":
            print("\nYou take the right path and find an abandoned hut.")
            encounter_random_event()
            continue
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue

        if treasure_found:
            find_treasure()
            break

if __name__ == "__main__":
    main_game()
