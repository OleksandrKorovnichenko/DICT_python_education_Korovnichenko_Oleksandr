"""The game "Gallows", the user has to guess the word by spelling it out."""

import random
import sys

# list of the word to be guessed
words = ['python', 'java', 'javascript', 'php', "programming", "hangman", "computer", "developer", "game"]

# the number of permissible errors
max_attempts = 8


# choose a random word from the list
def choose_word():
    return random.choice(words)


# function of displaying the word in the terminal
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


# main menu of the game
def main_menu():
    print("Welcome to the game HANGMAN")

    # if the player enters "play", the game starts, and if "exit", the program ends
    while True:
        print('Type "play" to play the game, "exit" to quit: ')
        choice = input('> ').lower()
        if choice == 'play':
            play_game()
        elif choice == 'exit':
            print("Goodbye!")
            sys.exit()
        else:
            print("Incorrect selection. Enter 'play' or 'exit'.")


# the logic of the game
def play_game():
    word_to_guess = choose_word()
    guessed_letters = []  # list to keep track of guessed letters
    attempts = 0

    print("Let's get started!")

    # number of attempts = 8
    # as long as the number of attempts is less than 8, the player has a chance to win
    while attempts < max_attempts:
        guessed_word = display_word(word_to_guess, guessed_letters)
        print(f'Guess the word:> {guessed_word}')

        if guessed_word == word_to_guess:
            print('')
            print("You survived!")
            print('')
            print("Thanks for playing!")
            print('')
            break

        guess = input('> ').lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed this letter.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
            else:
                attempts += 1
                print(f"Wrong guess!")
                print(f"That letter doesn't appear in the word. You have {max_attempts - attempts} attempts left.")
        else:
            print("Please enter a single letter.")

    if attempts == max_attempts:
        print("You lost!")
        print('')
        print("Thanks for playing!")
        print('')

    main_menu()


main_menu()
