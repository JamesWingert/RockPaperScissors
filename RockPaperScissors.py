import random

print("Hello and welcome to Rock, Paper, Scissors tournament./n"
      "The tournament will be the best of 3 wins!/n"
      "It will be you against our highly intelligent computer opponent!/n"
      "Good luck!")

while True:
    user_choice = int(input("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n"))

    if user_choice > 3 or user_choice < 1:
        user_choice = int(input("Please enter a valid input, 1,2 or 3:"))

    if user_choice == 1:
        choice_name = 'Rock'
    elif user_choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

