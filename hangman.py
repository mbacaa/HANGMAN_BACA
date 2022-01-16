from words import words
import random
import string
from drawings import drawings

def wordValidation(words):
    word = random.choice(words)    
    while word.isalpha() is False:
        word = random.choice(words)
    secretWord = word.upper()
    return secretWord

def main():
    secretWord = wordValidation(words)
    secretWord_letters = set(secretWord)
    used_letters = set() 
    alphabet_upper = set(string.ascii_uppercase)
    lives = 6

    while lives > 0 and len(secretWord_letters) > 0:
        if len(secretWord_letters) == 0:
            print("You guessed the word. Congratulations!")
        else:    
            player_input = input('Guess a letter: ').upper()
            if player_input in alphabet_upper:
                used_letters.add(player_input)
                if player_input in secretWord_letters:
                    secretWord_letters.remove(player_input)
                else:
                    lives -= 1
                    print("Wrong guess! You've got", lives, "lives left.")
            elif player_input in used_letters:
                print("Choose the other letter.")
            else:
                print("It isn't a letter!")
    print("You lost!")    

main()
