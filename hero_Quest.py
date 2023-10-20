import time

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def game_over():
    print_slow("Game Over! You have failed the quest.")
    exit(0)

def start_game():
    print_slow("You find yourself in a darck forrest.")  # Intentional typo
    choice = input("Do you want to go 'left' or 'right'? ").lower()
    
    if choice == 'left':
        print_slow("You encounter a hungry wolf. What will you do?")
        choice = input("Type 'fight' or 'run': ").lower()
        if choice == 'fightt':  # Intentional typo
            print_slow("You engage in a fierse battle with the wolf.")  # Intentional typo
            print_slow("Congratulations! You defeated the wolf and continue your journey.")
        else:
            print_slow("You choose to run, but the wolf is faster and catches you.")
    elif choice == 'rightt':  # Intentional typo
        print_slow("You follow the path to the rightt and come across a river.")  # Intentional typo
        choice = input("Will you 'swim' accross or 'find a bridge'? ").lower()  # Intentional typo
        if choice == 'find a bridgee':  # Intentional typo
            print_slow("You locate a sturdy bridge and safely cross the river.")
            print_slow("You continue your adventure.")
        else:
            print_slow("You attempt to swim, but the strong current pulls you away.")
            game_over()
    else:
        print_slow("Invalid choice. Please type 'left' or 'right'.")
        # Intentional logic error: The function is recursively called without an exit condition.
        start_game()

start_game()
