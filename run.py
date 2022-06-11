# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# External import statements 
import random

# Import statements I created for the game
from words import english_words
from words import spanish_words
from words import french_words
from display import display_hangman

# Welcome message to Hangman game
def type_name():
    """
    Welcome message and input player name to the console
    """
    print("###################################################################")
    print("                       HANGMAN")
    print("Choose your preferred language and guess the word to win the game!")
    print("###################################################################")

    # Print players name with welcome message
    while True:
        player_name = input("\033[0;36mEnter your name here: ").strip()

        if validate_name(player_name):
            print(f"Hello {player_name} welcome to my game\n")
            break

    # Game wont run without a name
    def validate_data(name):
    """
    Validates user data for name
    """

    try:
        if name == "":
            raise ValueError("\033[0;31mPlease input a name \n")
        elif len(name.strip()) == 0:
            raise ValueError("\033[0;31mPlease input a name \n")

    except ValueError as error:
        print(f"\033[0;31mPlease try again. {error}")
        return False

    return True



