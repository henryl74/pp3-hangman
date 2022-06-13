# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# External import statements 
import random
import os
import sys

# Import statements I created for the game
from words import english_words
from words import spanish_words
from words import french_words
from display import display_hangman

# Welcome message to Hangman game
def input_name():
    """
    Welcome message and input player name to the console
    """
    print(":::::::::::::::::::::::::::::::::::::")
    print("           HANGMAN")
    print("Choose your preferred language and")
    print("guess the word to win the game!")
    print(":::::::::::::::::::::::::::::::::::::")

    # Print players name with welcome message
    while True:
        player_name = input("\033[0;36mEnter your name here: \n").strip()

        if validate_name(player_name):
            print(f"Hello {player_name} welcome to my game \n")
            break

    # Game wont run without a name
def validate_name(name):
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

# Main menu structure

def main_menu():
    """
    Main menu options for the game and instructions 
    """
    print("\033[0mHangman Main Menu: \n")
    print("1. Hangman Instructions")
    print("2. Select the language to start the game")
    print("3. Exit Game \n")

    while True:
        menu_selection = input("\033[0;36mPlease select an option from the above menu: \n")

        if menu_selection == "1":
            hangman_instructions()
        elif menu_selection == "2":
            select_language()   
        elif menu_selection == "3":
            exit_game()
        else:
            print("\033[0;31mIncorrect input, please select a valid option from the menu.")

# Instructions explaining how to play the game

def hangman_instructions():
    """
    Game instructions for the player 
    """

    print(
        "\n\n"
        "\033[0;32mHow to Play Hangman: \n\n"
        "The main objective of this game "
        "is to make the correct word "
        "by guessing the correct letter one at a time. \n\n1. There are three languages "
        "you can choose to play this game: English, French and Spanish. \n2. To guess the word, "
        "type a letter of your choice on the selected language, then click the enter key. \n3. If your "
        "selection is correct the letter will be displayed on the screen. \n4. If the letter selected "
        "is wrong, the hangman will start to appear on the screen. \n5. You are given "
        "six attemps to get it right before the game is over. \n6. Click on run the program "
        "at the top of the screen to reset the whole game back to the beginning. \n\n"
    )

    # Prompts the player to start the game
    print("\033[0;36mAre you ready to have fun?.. if so then type 2 on your screen! \n")
    print("\033[0;36mOtherwise type 3 to exit the game. \n")

# Function to select the language for the game
def select_language():
    """
    Gives the player the option to choice a language to play the game
    and generates a ramdon word from local import file words.py
    """

    while True:
        language = input("\033[0;36mType option 1 for English words, 2 for Spanish words, and 3 for French words: \n")

        if language == "1":
            word = random.choice(english_words)
            start_hangman(word)
        elif language == "2":
            word = random.choice(spanish_words)
            start_hangman(word)
        elif language == "3":
            word = random.choice(french_words)
            start_hangman(word)

        else:
            print("\033[0;31mPlease try again!")

    def start_hangman(word):
        """
        Ramdon words from local import words.py will be used for the game 
        """


# Exit the Game function
def exit_game():
    """
    Exit game function and explains the player 
    how to reset the game back to the beginning
    """
    print("\033[0;36mThank you for playing Hangman, I hope you'll come back for more fun soon!")
    print("\033[0;36mIf you want to start over click the Run Program button at the top of the screen.")
    sys.exit()


def hangman_game():
    """
    Last function used to call all functions in the game
    """
    input_name()
    main_menu()
    select_language()
    start_hangman()

hangman_game()