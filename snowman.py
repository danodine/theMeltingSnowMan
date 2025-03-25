import random

STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    word_text= 'Word: ' + ('_ ' * len(secret_word))
    print(word_text)
    return mistakes + 1


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    mistakes = 0
    guess = ''
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    while mistakes < 3:
        # For now, simply prompt the user once:
        mistakes = display_game_state(mistakes, secret_word, guess)
        guess = input("Guess a letter: ").lower()


if __name__ == "__main__":
    play_game()