# This script is a number guessing game where the user has to guess a randomly chosen number between 1 and 1000.

import random

# Generate a random number between 1 and 1000 and store it in 'secretNumber'
secretNumber = random.randint(1, 1000)

# Prompt the user to choose a number between 1 and 1000
print('Choose a number between 1 and 1000')

# Allow the user up to 9 guesses
for guessesTaken in range(1, 10):
    # Read the user's guess and convert it to an integer
    guess = int(input())

    # Check if the guess is lower than the secret number
    if guess < secretNumber:
        print('Too low')
    # Check if the guess is higher than the secret number
    elif guess > secretNumber:
        print('Too high')
    # If the guess is correct, exit the loop
    else:
        break  # This condition is for the correct guess

# Check if the guess was correct
if guess == secretNumber:
    # Inform the user how many attempts it took to guess correctly
    print('You guessed the number in ' + str(guessesTaken) + ' attempts!')
else:
    # Inform the user of the correct number if they didn't guess it
    print('Sorry, the correct number was ' + str(secretNumber))
