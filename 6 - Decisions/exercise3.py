# Write a program that asks for two numbers. If the sum of the numbers is greater than 100, print "That is a big number."

print("This program will ask for two numbers.")
x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))
if x + y > 100:
    print(x + y, "is a big number!")
else:
    print("You get", x + y)
