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

def menu_rules():
    """
    Main menu options for the game and rules explaining how to play 
    """
    print("\033[0mHangman Main Menu: \n")
    print("1. Hangman Instructions")
    print("2. Select the language for the words")
    print("3. Start Hangman")
    print("4. Exit Game \n")

    while True:
        menu_selection = input("\033[0;36mPlease select an option from the above menu:")

        if menu_selection == "1":
            hangman_instructions()
        elif menu_selection == "2":
            select_language()
        elif menu_selection == "3":
            select_word()   
        elif menu_selection == "4":
            exit_game()
        else:
            print("\033[0;31mIncorrect input, please select a valid option from the menu")




