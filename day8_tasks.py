# Learning python basics
# GDSC 30 days challenge

# 1- Guessing Number Game

import random

def game() :
    print("Welcome ! this is a Guessing Game : ")
    rand_number = random.randint(1, 100)
    print("All you have to do to win this game is guessing the secret number the computer chose between 1 and 100 ")
    guess_number = 0
    attempt = 1

    while(guess_number != rand_number):
        guess_number = int(input("Enter the number that the computer chose : "))
        if(guess_number > rand_number):
            print("The computer's number is lower than yours !")
        elif (guess_number < rand_number):
            print("The computer number is greater than yours !")
        else:
            print(f"Congratulations ! You win after {attempt} attempts !")
            choice = input("Do you want to start a new game ? : ")
            if (choice.lower() == 'yes'):
                game()
            else:
                break
        attempt += 1


game()

# 2- Rock, Paper, Scissors Game

print("This game is a Rock, Paper, Scissor Game !")

def rps_game():
    computer_number = random.randint(1, 3)
    computer_choice = ''
    if (computer_number == 1):
        computer_choice = 'rock'
    elif (computer_choice == 2):
        computer_choice = 'paper'
    else:
        computer_choice = 'scissor'

    user_choice = input("Rock, Paper, Scissor ? : ")
    
    print(f"Computer does choose : {computer_choice}")
    if (user_choice.lower() == computer_choice):
        print("Draw ! you must restart !\n")
        rps_game()
    elif (computer_choice == 'rock' and user_choice.lower() == 'scissor'):
        print(f"You lose ! {computer_choice} smashes {user_choice}")
    elif (computer_choice == 'rock' and user_choice.lower() == 'paper'):
        print(f"Good Job ! You won ! {user_choice} wraps {computer_choice}")
    elif (computer_choice == 'scissor' and user_choice.lower() == 'paper'):
        print(f"You lose ! {computer_choice} cuts {user_choice}")
    elif (computer_choice == 'scissor'and user_choice.lower() == 'rock'):
        print(f"You won ! {user_choice} smashes {computer_choice}")
    elif (computer_choice == 'paper' and user_choice.lower() == 'rock'):
        print(f"You lose ! {computer_choice} wraps {user_choice}")
    elif (computer_choice == 'paper' and user_choice.lower() == 'scissor'):
        print(f"You won ! {user_choice} cuts {computer_choice}")
    else:
        print("This should be impossible")


rps_game()
