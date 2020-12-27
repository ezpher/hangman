#! python3

import string

# functions
def play(word):

    word_letters = set(word)
    alphabet_letters = set(string.ascii_uppercase)
    used_letters = list()
    tries = 6

    print()
    print("Let's play hangman: ")
    print(f'You have {tries} tries: ')

    while len(word_letters) > 0 and tries > 0:

        guessed_word = [letter if letter in used_letters else '-' for letter in word]

        print()
        print('Guessed Word: ', ' '.join(guessed_word))
        print('Used Letters: ', ' '.join(used_letters))

        guessed_letter = input('Guess a letter: ').upper()

        if guessed_letter in alphabet_letters and guessed_letter not in used_letters:
            used_letters.append(guessed_letter)

            if guessed_letter in word_letters:
                word_letters.remove(guessed_letter)
                print(f'The letter {guessed_letter} has been guessed correctly')
            else:
                print('Try again. The letter is not in the word.')

                tries -= 1
                print(f'Tries left: {tries}')

        elif guessed_letter in used_letters:
            print('Letter has been used')

        else:
            print('Not a valid letter')

            tries -= 1
            print(f'Tries left: {tries}')

    print()
    if tries == 0:
        print('You have no more tries left')
    else:
        print('You have guessed the word correctly!')

def main(word):
    play(word)
    while input("Play again? (Y/N): ").upper() == 'Y':
        play(word)

# main
if __name__ == '__main__':    

    word = 'SUBTEFUGE'
    main(word)



