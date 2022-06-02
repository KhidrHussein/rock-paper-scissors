from random import choice
is_on = True

while is_on:
    user_choice = input("What do you choose? Type R for Rock, P for Paper or S for Scissors.\n").lower()
    computer_choice = choice(['R', 'P', 'S']).lower()
    print("Computer chose:")
    print(computer_choice)
    if user_choice != 'r' and user_choice != 'p' and user_choice != 's': 
        print("You typed a wrong choice, you lose!") 
    elif user_choice == 'r' and computer_choice == 's':
        print("You win!")
        is_on = False
    elif computer_choice == 'r' and user_choice == 's':
        print("You lose!")
    elif computer_choice == 'p' and user_choice == 's':
        print("You win!")
        is_on = False
    elif user_choice == 'p' and computer_choice == 's':
        print("You lose!")
    elif computer_choice == 'r' and user_choice == 'p':
        print("You win!")
        is_on = False
    elif user_choice == 'p' and computer_choice == 'r':
        print("You lose!")
    elif computer_choice == user_choice:
        print("It's a draw")

