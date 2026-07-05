# Q2: Create a number guessing game where the computer generates a random number,
# and the user keeps guessing until the correct number is found. Display hints
# to guess higher or lower and show the total number of attempts taken.

import random

# Generate a random number between 1 and 100
jackpot = random.randint(1, 100)

# Take the first guess from the user
guess = int(input('Guess the number: '))

# Counter to track the number of attempts
count = 1

# Continue looping until the correct number is guessed
while jackpot != guess:

    # Hint: Guess a higher number
    if jackpot > guess:
        print('Wrong Guess! Try Higher')
        count += 1

    # Hint: Guess a lower number
    else:
        print('Wrong Guess! Try Lower')
        count += 1

    # Take another guess from the user
    guess = int(input('Guess the number: '))

# Display success message and total attempts
print('Correct Jackpot, you completed the guess in', count, 'attempts')