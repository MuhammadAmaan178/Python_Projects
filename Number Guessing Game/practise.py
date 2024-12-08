"""
Number Guessing Game
"""

import random

with open("high_score.txt","r") as f:
    high_score = int(f.read())

comp_c = random.randint(1,50)
attempts = 0
print("I am thinking a number between 1 to 50")

while True:
    # Get the user's guess
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Increment the attempt counter
    attempts += 1

    # Check the guess and provide feedback
    if (guess < comp_c):
        print("Too low! Try again.")
    elif (guess > comp_c):
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

if (attempts < high_score):
    with open("high_score.txt","w") as f:
        f.write(str(attempts))
