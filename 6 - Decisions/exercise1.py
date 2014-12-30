# Write a program that asks the user their name, if they enter your name say "That is a nice name", if they entere "John Cleese" or "Michael Palin", tell them how you feel about them.  Otherwise tell them "You have a nice name."

name = str(input("Hi there, what's your name? "))

if name == "gyratory":
    print("That's a swell name!")
elif name == "John Cleese" or name == "Micael Palin":
    print("Who the heck are you?")
else:
    print("That's a nice name!")
