from words import words
import random
import string


def valid_word(valid_words):
    while '-' or ' ' not in valid_words:
        word = random.choice(valid_words)
        return word.upper()


def hangman():
    word = valid_word(words)
    letters_in_word = set(word)
    alphabet = set(string.ascii_uppercase)
    letter_guesses_user = set()

    lives = 7

    while len(letters_in_word) > 0 and lives > 0:
        print("you have", lives, "left and you have used these letters",
              ' '.join(letter_guesses_user))

        displayed_word = [
            letter if letter in letter_guesses_user else '-' for letter in word]
        print("Current word: ", ' '.join(displayed_word))
        current_guess = (input("Guess a letter: ")).upper()
        if current_guess in alphabet-letter_guesses_user:
            letter_guesses_user.add(current_guess)
            if current_guess in letters_in_word:
                letters_in_word.remove(current_guess)

            else:
                lives = lives - 1
                print('\n your letter ', current_guess, 'is not in the word')

        elif current_guess in letter_guesses_user:
            print('\Already used this letter. Please try again')

        else:
            print("\nNot a valid letter.")

    if lives == 0:
        print("You are hanged. The correct word is ", word)
    else:
        print("\nYou have guessed the word correctly. ", word, "is the word")


hangman()
