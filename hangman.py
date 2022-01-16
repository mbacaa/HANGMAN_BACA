from words import words
import random
import string
from drawings import drawings

#pobieranie losowego hasła z listy słów, zamiana na wielkie litery, sprawdzenie czy zawiera poprawne znaki (tylko litery)
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
        
        player_input = input('Make a guess: ').upper()

        if len(player_input) > 1 and player_input != secretWord:
            lives -=1
            print(drawings[lives])
            print("Wrong guess! You've got", lives, "lives left.")
            continue
        
        if len(win_condition) != 0 and player_input != secretWord and lives != 0:    
            if player_input in used_letters:
                print("Choose the other letter.")
                continue            
            elif player_input in alphabet_upper:
                used_letters.add(player_input)
                if player_input in win_condition:
                    win_condition.remove(player_input)
                else:
                    lives -= 1
                    print("Wrong guess! You've got", lives, "lives left.")
                    print(drawings[lives])
            else:
                print("It isn't a letter!")
                continue

        #warunki zakończenia gry: 
        #wygrana gdy zostanie wpisane całe hasło lub zostaną odgadnięte wszystkie litery
        if len(win_condition) == 0 or player_input == secretWord:
            print("You guessed the secret word! Congratulations!")
            print(drawings['win'])
            break
        #przegrana gdy skończą się nam życia
        elif lives == 0:
            print("You lost!")
            print(drawings[lives])
            break

main()