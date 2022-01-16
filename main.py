from solver import wordValidation_Solver, main_Solver
from hangman import wordValidation_Hangman, main_Hangman
from words import words
from drawings import drawings
import random
import string
import time

menu = input("""
Type '1' for Player VS Bot \n
Type '2' for Bot vs Player
""")

if menu == '1':
    wordValidation_Hangman(words)
    main_Hangman()
elif menu == '2':
    wordValidation_Solver()
    main_Solver()
else:
    print("Wrong input!")