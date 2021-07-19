import random


def guess(x):
    # generates a random number which will be stored in variable random_number
    random_number = random.randint(1, x)
    guess = 0  # initializing the guess with zero so that the while loop can function!
    while guess != random_number:
        guess = int(input(f"guess a number between 1 & {x}:\n"))
        if guess > random_number:
            print("sorry your guess is too high,try again")
        elif guess < random_number:
            print("your guess is too low ")

    print(f"yay! you have a correct guess {guess}")


guess(10)
