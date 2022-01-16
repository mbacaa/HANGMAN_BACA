import random
import string
from drawings import drawings
import time

#wpisanie hasła, zamiana na wielkie litery, sprawdzenie czy zawiera poprawne znaki (tylko litery)
def wordValidation():
    word = input('Give me a word: ')    
    while word.isalpha() is False:
        word = input('Give me a CORRECT word: ') 
    secretWord = word.upper()
    return secretWord

def main():
    secretWord = wordValidation()
    secretWord_letters = set(secretWord)
    alphabet_upper = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    win_condition = secretWord_letters.copy()

    while lives > 0 and len(win_condition) > 0:
        #"mechanizm" wypisywania podkreśleń/liter w haśle
        for secretWord_letters in secretWord:
            if secretWord_letters in used_letters:
                print(secretWord_letters, " ", end='')
            else:
                print("_ ", end='')
        
        #główna pętla
        print('\n')
        if len(used_letters) != 0:
            print("Used letters:", used_letters)
            time.sleep(2.5)
        
        letter = random.choice(string.ascii_uppercase)
        while letter in used_letters:
            print("Choose the other letter.")
            letter = random.choice(string.ascii_uppercase)
        
        bot_input = used_letters.add(letter)
        print("Bot guess: ", letter)
        time.sleep(2.5)

        if len(win_condition) != 0 and lives != 0:              
            if letter in alphabet_upper:
                if letter in win_condition:
                    win_condition.remove(letter)
                else:
                    lives -= 1
                    print("Wrong guess! You've got", lives, "lives left.")
                    print(drawings[lives])
            else:
                print("It isn't a letter!")
                continue

        #warunki zakończenia gry: 
        #wygrana gdy zostanie wpisane całe hasło lub zostaną odgadnięte wszystkie litery
        if len(win_condition) == 0 or letter == secretWord:
            print("You guessed the secret word! Congratulations!")
            print(drawings['win'])
        #przegrana gdy skończą się nam życia
        elif lives == 0:
            print("You lost!")
            print(drawings[lives])

main()