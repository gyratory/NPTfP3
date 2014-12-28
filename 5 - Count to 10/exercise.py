# Write a program that asks the user for a Login Name and password. Then when they type "lock", they need to type in their name and password to unlock the program.
user = str(input("Please provide a loginname: "))
unlock_user = str()
password = str(input("Please provide your password: "))
unlock_pw = str()
lock = str()

#while lock != "unlock":
#    lock = input("The console is now locked. \nYou will be prompted to enter your username and password. \nTo unlock, enter 'unlock': ")
print("To lock your computer type 'lock'.")
while lock != "lock":
    lock = input("What is your command? ")
while unlock_user != user:
    unlock_user = input("Enter your Username: ")
while unlock_pw != password:
    unlock_pw = input("Enter your Password: ")
print("Welcome to the Accelerated World,", user + ".")
