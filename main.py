print("Welcome to the rollercoaster!")
height = int(input("First we need to check your height, How tall are you in cm? "))
bill = 0

if height >= 150:
    print("Great! You can ride! ")
    age = int(input("How old are you? "))
    if age <=18:
        print("Your ticket will cost $7 ")
        bill += 7
    elif age < 12:
        print("Your ticket will cost $5")
        bill +=5
    else:
        print("Your ticket will cost $12")
        bill += 12
    photo = input("Would you like to purchase a photo for $3? y or n ")
    if photo == "y":
        bill += 3
        print(f"Your total is {bill}")
    else:
        print(f"Your total is {bill}")


else:
    print("Sorry you aren't tall enough...come back after you grow. ")