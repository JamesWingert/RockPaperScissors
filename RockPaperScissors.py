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
    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print(f"Computer has chosen: {comp_choice_name}")
    comp_count = 0
    user_count = 0

    while (comp_count < 3) and (user_count < 3):

        if user_choice == 1 and comp_choice == 2:
            comp_count += 1
            print("Computer wins this round with Paper! "
                  f"\n Computer: {comp_count}"
                  f"\n You: {user_count} ")

        elif user_choice == 1 and comp_choice == 3:
            user_count += 1
            print("You win this round with Rock!"
                  f"\n Computer: {comp_count}"
                  f"\n You: {user_count} ")

        elif user_choice == 2 and comp_choice == 1:
            user_count += 1
            print("You win this round with Paper!"
                  f"\n Computer: {comp_count}"
                  f"\n You: {user_count} ")

        elif user_choice == 2 and comp_choice == 3:
            comp_count += 1
            print("Computer wins this round with Scissor!"
                  f"\n Computer: {comp_count}"
                  f"\n You: {user_count} ")

        elif user_choice == 3 and comp_choice == 2:
            user_count += 1
            print("You win this round with Scissor!"
                  f"\n Computer: {comp_count}"
                  f"\n You: {user_count} ")

        elif user_choice == 3 and comp_choice == 1:
            user_count += 1
            print("Computer wins this round with Rock!"
                  f"\n Computer: {comp_count}"
                  f"\n You: {user_count} ")

        else:
            print(f"This round was a tie! Both choosing {user_choice_name}, try again!"
                  f"\n Computer: {comp_count}"
                  f"\n You: {user_count} ")
    elif user_count == 2:
        print('test1')
    elif comp_count == 2:
        print('test2')
