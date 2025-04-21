# SNAKE WATER GUN GAME

import random

computer_options = ["snake", "water", "gun"]
score_computer = 0
score_user = 0
turns = 0

print("Welcome to the Python Snake, Water, and Gun game.")

while turns < 5:
    user_choice = input('''
'S' for snake.
'W' for water.
'G' for gun.
'Q' for quit.

Your choice: ''').lower()
    
    if user_choice == "q":
        print("Thanks for playing! Exiting the game.")
        break

    if user_choice not in ['s', 'w', 'g']:
        print("Invalid input! Please choose 'S', 'W', 'G', or 'Q'.")
        continue

    computer_choice = random.choice(computer_options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == "s":
        if computer_choice == "gun":
            print("Computer wins! Gun shoots the snake.")
            score_computer += 1
        elif computer_choice == "water":
            print("You win! Snake drinks water.")
            score_user += 1
        else:
            print("It's a draw!")

    elif user_choice == "w":
        if computer_choice == "snake":
            print("Computer wins! Snake drinks water.")
            score_computer += 1
        elif computer_choice == "gun":
            print("You win! Gun sinks in water.")
            score_user += 1
        else:
            print("It's a draw!")

    elif user_choice == "g":
        if computer_choice == "water":
            print("Computer wins! Gun sinks in water.")
            score_computer += 1
        elif computer_choice == "snake":
            print("You win! Gun shoots the snake.")
            score_user += 1
        else:
            print("It's a draw!")
    
    turns += 1
    print(f"Score - You: {score_user}, Computer: {score_computer}")

# Final Results
print("\nGame Over!")
if score_user > score_computer:
    print(f"Congratulations! You won the game with a score of {score_user} to {score_computer}.")
elif score_user < score_computer:
    print(f"Computer wins! Final score: {score_computer} to {score_user}.")
else:
    print(f"It's a tie! Final score: {score_user} to {score_computer}.")
