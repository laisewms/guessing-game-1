"""A number-guessing game."""

# Put your code here
import random
def guess_number():
    # greet player
    print('Welcome to the guessing game!')
# get player name
    players_name = input("What is your name? ")
    print(f"Let's start it {players_name}!!")
# choose random number between 1 and 100
    secret_num = random.randint(1,100)
    players_guess = 0 
# repeat forever:
    while players_guess != secret_num:
        players_guess = int(input("What is your guess? "))
        if players_guess > secret_num:
            print("the number is too HIGH!")
            
        elif players_guess < secret_num:
            print("The number is too LOW!")
        
    else:
        print("You got it! Congrats!!")
        print("yaaaaaaaay!!!")
    
    
    

       

guess_number()
