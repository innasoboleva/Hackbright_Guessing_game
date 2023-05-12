"""A number-guessing game."""

import random

user_name = input("What is your name? ")
print(f"Hi {user_name}!")
tries = 0

number = random.randint(1, 100)
print("Jessica, I'm thinking of a number between 1 and 100.\n")
print("Try to guess my number.\n")


while True:
    your_guess = input("Your guess? ")
    if your_guess.isdigit():
        your_guess1 = int(your_guess)
        tries += 1
        if your_guess in range(1,101):
            if your_guess1 is number:
                print(f"Well done, {user_name}! You found my number in {tries} tries!")
                break
            else:
                if your_guess1 > number:
                    print("Your guess is too high, try again.")
                else:
                    print("Your guess is too low, try again.")
        else:
            print("Your input is invalid! Please try again!")       
    else:
        print("Wrong input, please try again") 