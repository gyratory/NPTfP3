# Write a program that has a user guess your name, but they only get 3
# chances to do so until the program quits.

print("=========")
print("You will now try to guess my name!\nYou have 3 tries.")
print("=========")
attempt = 0
while attempt != 3:
    attempt += 1
    guess = input("Take a guess: ")
    if guess == "gyratory":
        print("Congratulations! You win nothing.")
        quit()
    elif attempt <= 2:
        print("Try again.")
    else:
        print("You failed!")
