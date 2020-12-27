#! python3

import string

word = 'SUBTEFUGE'
word_letters = set(word)
alphabet_letters = set(string.ascii_uppercase)
used_letters = set()

while len(word_letters) > 0:

    guessed_word = [letter if letter in used_letters else '-' for letter in word]

    print()
    print('Guessed Word: ', ' '.join(guessed_word))
    print('Used Letters: ', ' '.join(used_letters))

    guessed_letter = input('Guess a letter: ').upper()

    if guessed_letter in alphabet_letters - used_letters:
        used_letters.add(guessed_letter)

        if guessed_letter in word_letters:
            word_letters.remove(guessed_letter)
            print(f'The letter {guessed_letter} has been guessed correctly')
        else:
            print('Try again. The letter is not in the word.')

    elif guessed_letter in used_letters:
        print('Letter has been used')

    else:
        print('Not a valid letter')

print('You have guessed the word correctly!')

