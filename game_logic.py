from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

DASHES = []

def start_game():
    pass


def game_ended(mistakes, word, secret_word):
    game_has_ended = False

    if mistakes == 3:
        print('You lose')
        game_has_ended = True

    if word == secret_word:
        print('You win')
        game_has_ended = True
        mistakes = 3

    if game_has_ended:
        input_valid = False
        while not input_valid:
            new_game = input('Do you want to play again Y/N: ')
            if new_game == 'y' or new_game == 'Y':
                play_game()
            elif new_game != 'N' and new_game != 'n':
                input_valid = False
    return mistakes


def display_game_state(mistakes, secret_word, guessed_letters):
    word = ''
    if guessed_letters in secret_word:
        for key, letter in enumerate(secret_word):
            if guessed_letters == letter:
                DASHES[key] = guessed_letters
    else:
        print(1)
        mistakes += 1

    print(STAGES[mistakes])

    for dash in DASHES:
        word += dash
        print(dash, end=' ')

    print()

    mistakes = game_ended(mistakes, word, secret_word)

    return mistakes


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    mistakes = 0
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)
    for _ in range(len(secret_word)):
        DASHES.append('-')

    print(STAGES[0])
    print('_ '*len(secret_word))
    while mistakes < 3:
        guess = input("Guess a letter: ").lower()
        if len(guess) < 2 and guess.isalpha():
            mistakes = display_game_state(mistakes, secret_word, guess)
        else:
            print('Invalid input please enter 1 letter!')

