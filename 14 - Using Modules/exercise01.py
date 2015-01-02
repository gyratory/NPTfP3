# Rewrite the high_low.py program from section Decisions to use an random
# integer between 0 and 99 instead of the hard-coded 78. Use the Python
# documentation to find an appropriate module and function to do this.

# Plays the guessing game higher or lower
import random
number = random.randint(0, 99)
guess = -1
print("Guess the number!")
while guess != number:
    guess = int(input("Is it... "))
    if guess == number:
        print("Hooray! you guess it right!")
    elif guess < number:
        print("It's bigger...")
    else:
        print("It's not so big.")
