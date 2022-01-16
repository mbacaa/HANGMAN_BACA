from solver import wordValidation_Solver, main_Solver
from hangman import wordValidation_Hangman, main_Hangman
from words import words
import random
import string
from drawings import drawings
import time

menu = 0

while menu != 3:
    menu = input("""
        Type 'P' for Player VS Bot
        Type 'B' for Bot vs Player
        Type 'Q' to Quit
        """).upper()
    if menu == 'P':
        wordValidation_Hangman(words)
        main_Hangman()
        print(menu)
    elif menu == 'B':
        wordValidation_Solver()
        main_Solver()
    elif menu == 'Q':
        break
    else:
        print("Wrong input!")