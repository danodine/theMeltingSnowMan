from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Placeholder for displayed letters
DASHES = []


def game_ended(mistakes, word, secret_word):
    """
    Checks if the game has ended, prints win/lose message, and offers to restart the game.

    Args:
        mistakes (int): Current number of mistakes.
        word (str): Current guessed word with dashes and letters.
        secret_word (str): The word to guess.

    Returns:
        int: Updated mistake count.
    """
    game_has_ended = False

    if mistakes == 3:
        print("You lose")
        game_has_ended = True

    if word == secret_word:
        print("You win")
        game_has_ended = True
        mistakes = 3

    if game_has_ended:
        input_valid = False
        while not input_valid:
            new_game = input("Do you want to play again? Y/N: ").strip().lower()
            if new_game == 'y':
                DASHES.clear()
                play_game()
                input_valid = True
            elif new_game == 'n':
                input_valid = True
            else:
                print("Invalid input. Please enter Y or N.")

    return mistakes


def display_game_state(mistakes, secret_word, guessed_letter):
    """
    Updates and displays the game state based on the player's guess.

    Args:
        mistakes (int): Current number of mistakes.
        secret_word (str): The word to guess.
        guessed_letter (str): The letter guessed by the player.

    Returns:
        int: Updated mistake count.
    """
    word = ''

    if guessed_letter in secret_word:
        for index, letter in enumerate(secret_word):
            if guessed_letter == letter:
                DASHES[index] = guessed_letter
    else:
        print("Wrong guess!")
        mistakes += 1

    print(STAGES[mistakes])

    for dash in DASHES:
        word += dash
        print(dash, end=' ')
    print()

    mistakes = game_ended(mistakes, word, secret_word)

    return mistakes


def play_game():
    """
    Starts and runs the game loop.
    """
    mistakes = 0
    secret_word = random.choice(WORDS)

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected:", secret_word)  # Optional: remove in production
    DASHES.clear()
    for _ in range(len(secret_word)):
        DASHES.append('-')

    print(STAGES[0])
    print('_ ' * len(secret_word))

    while mistakes < 3:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            mistakes = display_game_state(mistakes, secret_word, guess)
        else:
            print("Invalid input. Please enter a single letter.")
