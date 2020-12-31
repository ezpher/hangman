#! python3

import random
import string
from words import word_list

# functions

def get_word():
    word = random.choice(word_list)
    word = ''.join([letter.upper() for letter in word])
    return word

def play(word):

    word_letters = set(word)
    alphabet_letters = set(string.ascii_uppercase)
    used_letters = list()
    tries = 6

    print()
    print("Let's play hangman: ")

    while len(word_letters) > 0 and tries > 0:

        guessed_word = [letter if letter in used_letters else '-' for letter in word]

        print()
        print(display_hangman(tries))
        print(f'Tries left: {tries}')
        print('Guessed Word: ', ' '.join(guessed_word))
        print('Used Letters: ', ' '.join(used_letters))

        guessed_letter = input('Guess a letter: ').upper()

        print()
        if guessed_letter in alphabet_letters and guessed_letter not in used_letters:
            used_letters.append(guessed_letter)

            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
                print(f'The letter {guessed_letter} has been guessed correctly')
            else:
                print('Try again. The letter is not in the word.')
                tries -= 1

        elif guessed_letter in used_letters:
            print('Letter has been used')

        else:
            print('Not a valid letter')
            tries -= 1

    print()
    if tries == 0:
        print('You have no more tries left')
    else:
        print('You have guessed the word correctly!')
    print(f"The word is {word}")

def display_hangman(tries):

    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

    return stages[tries]

def main(word):
    word = get_word()
    play(word)
    while input("Play again? (Y/N): ").upper() == 'Y':
        word = get_word()
        play(word)

# main
if __name__ == '__main__':    

    word = 'SUBTEFUGE'
    main(word)



