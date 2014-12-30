#! /usr/bin/python
#-*-coding: utf-8 -*-
# Rewrite the area2.py program from the Examples above to have a separate function for the area of a square, the area of rectangle, and the area of a circle (3.14 * radius**2). This program should include a menu interface.

def print_options():
    print("Options: ")
    print(" 'c' to approximate the area of a circle")
    print(" 'r' to calculate the area of a rectangle")
    print(" 's' to calculate the area of a square")
    print(" 'q' to quit the program")

def area_r(width, height):
    return width * height

def area_s(side):
    return side ** 2

def area_c(radius):
    return 3.14 * radius ** 2

def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Must be a positive number')
        number = float(input(prompt))
    return number

choice = 'p'
while choice != 'q':
    if choice == 'c':
        r = float(input('Enter the radius of your circle: '))
        print('The area of your circle is approximately:', area_c(r))
        choice = input('option: ')
    elif choice == 'r':
        w = float(input('Enter the width of your rectangle: '))
        h = float(input('Enter the height of your rectangle: '))
        print('The area of your rectangle is:', area_r(w, h))
        choice = input('option: ')
    elif choice == 's':
        s = float(input('Enter the length of a side of your square: '))
        print('The area of your square is:', area_s(s))
        choice = input('option: ')
    elif choice != "q":
        print_options()
        choice = input("option: ")
