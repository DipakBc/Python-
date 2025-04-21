# The perfect guess.

import random

randomNumber = random.randrange(1, 10)
numberOfGuess = 0

while numberOfGuess < 10:
    try:
        userGuess = int(input("Enter your guess (1-10): "))
        numberOfGuess += 1  # Increment after a valid input
        if userGuess > randomNumber:
            print("Your guess is too high. Try a lower number.")
        elif userGuess < randomNumber:
            print("Your guess is too low. Try a higher number.")
        else:
            print(f"Perfect guess! The number was {randomNumber}.")
            print(f"You guessed it in {numberOfGuess} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
else:
    print(f"Sorry! You've used all your attempts. The number was {randomNumber}.")