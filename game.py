"""A number-guessing game."""

import random

user_name = input("What is your name? ")
print(f"Hi {user_name}!")
tries = 0

number = random.randint(1, 100)
print(f"{user_name}, I'm thinking of a number between 1 and 100.\n")
print("Try to guess my number.\n")


while True:
    your_guess = input("Your guess? ")
    if your_guess.isdigit():
        guess = int(your_guess)
        tries += 1
        if guess in range(1,101):
            if guess == number:
                print(f"Well done, {user_name}! You found my number in {tries} tries!")
                break
            else:
                if guess > number:
                    print("Your guess is too high, try again.")
                else:
                    print("Your guess is too low, try again.")
        else:
            print("Your input is invalid! Please try again!")       
    else:
        print("Wrong input, please try again") 
