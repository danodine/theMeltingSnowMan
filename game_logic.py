from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

DASHES = []


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

    if word == secret_word:
        print('You win')
        mistakes = 3

    if mistakes == 3:
        print('You lose')
    return mistakes


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    mistakes = 0
    guess = ''
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    for _ in range(len(secret_word)):
        DASHES.append('-')

    print(STAGES[0])
    print('_ '*len(secret_word))
    # TODO: Build your game loop here.
    while mistakes < 3:
        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        if len(guess) < 2 and guess.isalpha():
            mistakes = display_game_state(mistakes, secret_word, guess)

