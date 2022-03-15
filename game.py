"""A number-guessing game."""

# Put your code here
import random
def guess_number():
    num_to_find = random.randint(1,100)
    print('Welcome to the guessing game')
    players_name = input("What is your name? ")
    players_num = input(f"Hello, {players_name}! What is your guess? ")
