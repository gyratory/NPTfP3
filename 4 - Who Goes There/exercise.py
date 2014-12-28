# Write a program that gets 2 string variables and 2 number variables from the user, concatenates (joins them together with no spaces) and displays the strings, then multiplies the two numbers on a new line.

w1 = input("Please provide a word: ")
w2 = input("Please provide another word: ")
x = int(input("Please provide a number: "))
y = int(input("Please provide another number: "))
print("You've created the new word: ", w1 + w2 + "!")
print("The product of your numbers is", x * y)
