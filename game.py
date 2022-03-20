"""A number-guessing game."""

# Put your code here
import random

instructions = """
  (X)Play The Game
  (Q)Quit The Game
  """
def play_again():

    while True:
        print(instructions)
        choice = input('> ')
        choice.lower()

        if choice == 'x':
            print(guess_number())
        elif choice == 'q':
            print('see you')

        else: 
            print(f'{choice} is not an option')

def guess_number():
    
    # greet player
    print('Welcome to the guessing game!')
# get player name
    players_name = input("What is your name? ")
    print(f"Let's start it {players_name}!!")
# choose random number between 1 and 100
    secret_num = random.randint(1,100)
    players_guess = 0 

# variable to count the amount of guesses

    count_guesses= 0 
    
# repeat forever:
    
    while players_guess != secret_num:
        count_guesses += 1
        players_guess = int(input("What is your guess? "))
        if players_guess < 0 or players_guess > 100:
            print('pick a number between 1-100')
        elif players_guess > secret_num:
            print("the number is too HIGH!")
            
        elif players_guess < secret_num:
            print("The number is too LOW!")
        
    else:
        print("You got it! Congrats!!")
        print("yaaaaaaaay!!!")
        print(f"You had {count_guesses} tries.")
        print(play_again())


guess_number()



