# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Import statements I created for the game
from words import english_words
from words import spanish_words
from words import french_words

# External import statements
import random
from os import system, name
import sys
from time import sleep
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# Welcome message to Hangman game
def input_name():
    """
    Welcome message and input player name to the console
    """
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(Fore.YELLOW + r"""
  /\  /\ __ _  _ __    __ _  _ __ ___    __ _  _ __
 / /_/ // _` || '_ \  / _` || '_ ` _ \  / _` || '_ \
/ __  /| (_| || | | || (_| || | | | | || (_| || | | |
\/ /_/  \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_|
                      |___/
                      """)
    print(Fore.GREEN + "Welcome to my Game!")
    print(Fore.GREEN + "Choose your preferred language and")
    print(Fore.GREEN + "guess the word to win the game.")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::")

    # Print players name with welcome message
    while True:
        player_name = input(Fore.LIGHTBLUE_EX +
                            "Enter your name here: \n").strip()

        if validate_name(player_name):
            print(f"Hello {player_name} welcome to Hangman \n")
            break
    sleep(2)
    clear()
    main_menu()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


# Game wont run without a name
def validate_name(name):
    """
    Validates user data for name
    """
    try:
        if name == "":
            raise ValueError(Fore.LIGHTRED_EX + "Please input a name \n")
        elif len(name.strip()) == 0:
            raise ValueError(Fore.LIGHTRED_EX + "Please input a name \n")
        elif not name.isalpha():
            raise ValueError("error")

    except ValueError as error:
        print(Fore.LIGHTRED_EX + f"Please try again. {error}")
        return False

    return True


# Main menu structure
def main_menu():
    """
    Main menu options for the game and instructions
    """
    print(Fore.LIGHTYELLOW_EX + "Hangman Main Menu: \n")
    print("1. Hangman Instructions")
    print("2. Select the language to start the game")
    print("3. Exit Game \n")

    while True:
        menu_selection = input(Fore.LIGHTYELLOW_EX +
                               "Please select an option from the menu: \n")

        if menu_selection == "1":
            hangman_instructions()
            break
        elif menu_selection == "2":
            select_language()
            break
        elif menu_selection == "3":
            exit_game()
            break
        else:
            print(Fore.LIGHTYELLOW_EX +
                  "Incorrect, please select a valid option from the menu")


# Instructions explaining how to play the game
def hangman_instructions():
    """
    Game instructions for the player
    """
    clear()

    print(Fore.CYAN +
          "\n\n"
          "How to Play Hangman: \n\n"
          "The main objective of this game is to make the correct word "
          "by guessing the\n correct letter one at a time.\n"
          "\n1. There are three languages you can choose to play this game, "
          "these are: English, Spanish and French. "
          "\n2. To guess the word, type a letter of your choice "
          "on the selected language, then press the enter key. "
          "\n3. If your selection is correct "
          "the letter will be displayed on the screen "
          "\n4. If the letter selected is wrong, the hangman "
          "will start to appear on the screen. "
          "\n5. You are given SIX attemps to get it right "
          "before the game is over. "
          "\n6. If you get stuck running the game please click on "
          "run the program at the top of the screen, "
          "to reset the whole game back to the beginning. \n\n"
          )

    input("Press Enter to continue.")
    clear()
    main_menu()


# Function to select the language for the game
def select_language():
    """
    Gives the player the option to choice a language to play the game
    and generates a ramdon word from local import file words.py
    """

    while True:
        language = input(Fore.LIGHTCYAN_EX +
                         "Type 1 for English words,"
                         "\n2 for Spanish words, 3 for French words. \n")

        if language == "1":
            word = random.choice(english_words)
            start_hangman(word)
            break
        elif language == "2":
            word = random.choice(spanish_words)
            start_hangman(word)
            break
        elif language == "3":
            word = random.choice(french_words)
            start_hangman(word)
            break

        else:
            print(Fore.LIGHTRED_EX + "Please try again!")


# Function to start the game
def start_hangman(word):
    """
    Ramdon words from local import words.py will be used for the game
    """
    attempts = 6
    letters = set(word)
    guesses = []

    # Displays the right answer after all attempts
    while attempts > 0 and len(letters) > 0:
        display_answer = [
            letters if letters in guesses else "_" for letters in word
        ]
        print(hangman_status(attempts))
        print("\n")
        print(" ".join(display_answer))

        # Request the player to take their turn to guess a new letter
        # .upper used to capitalise letters to match the words from my lists
        player_guess = input(Fore.LIGHTWHITE_EX +
                             "Please choose a letter:\n").upper().strip()

        # Clear the terminal
        os.system("cls" if os.name == "nt" else "clear")

        # Validating the selection made
        if player_guess in guesses:
            print(Fore.LIGHTCYAN_EX +
                  "Sorry! You already guessed ", player_guess, "\n")
            print("You have used these letters: ")
            print(" ".join(guesses))

        # Check and validate one character per guess.
        elif len(player_guess) != 1:
            print(Fore.LIGHTRED_EX +
                  "Sorry! please only enter one guess at a time\n")
            print("You have used these letters: ")
            print(" ".join(guesses))

        # Makes sure the input is a letter only.
        elif not player_guess.isalpha():
            print(Fore.LIGHTRED_EX +
                  "Sorry! ", player_guess, " is not a letter\n")
            print("You have used the following letters: ")
            print(" ".join(guesses))
        elif player_guess not in word:
            print(Fore.LIGHTRED_EX +
                  "Please try again,", player_guess, "is not right")
            attempts -= 1
            print(Fore.LIGHTCYAN_EX + "Attempts Remaining: ", attempts)
            guesses.append(player_guess)
            print(Fore.LIGHTGREEN_EX + "You have used these letters: ")
            print(" ".join(guesses))
        else:
            print(Fore.LIGHTGREEN_EX + "Good job! \n")
            guesses.append(player_guess)
            print(Fore.LIGHTGREEN_EX + "You have used these letters: ")
            print(" ".join(guesses))
            if player_guess in letters:
                letters.remove(player_guess)
            else:
                print(Fore.LIGHTRED_EX + "Please make a valid choice.")

        # Displays the amounts of attempts left.
        if attempts == 0:
            print(Fore.LIGHTCYAN_EX + "Attempts Remaining: ", attempts)
            guesses.append(player_guess)
            print(Fore.LIGHTRED_EX + "Sorry you lose!")

    # Prompt the player if he/she want to try again.
    print("The correct word was", word, "\n")
    print(Fore.LIGHTCYAN_EX + "Would you like to try again?")
    play_again()


def play_again():
    """
    Player chooses to play again or exit to the menu.
    """
    while True:
        # Check and validate entry to continue in the game.
        try_again = input("Press 1 for Yes or 2 for No: ")

        if try_again == '1':
            select_language()
        elif try_again == '2':
            main_menu()
        else:
            print(Fore.LIGHTRED_EX + "Please make a valid choice.")


# Display the hangman stages

def hangman_status(tries):
    """
    Each status of the hangan
    """
    stages = [
        """
            +------+
            |      |
            |      o
            |     \\|/
            |      |
            |     / \\
            ===========
            """,
        """
            +------+
            |      |
            |      o
            |     \\|/
            |      |
            |     /
            ===========
            """,
        """
            +------+
            |      |
            |      o
            |     \\|/
            |      |
            |
            ===========
            """,
        """
            +------+
            |      |
            |      o
            |     \\|
            |      |
            |
            ===========
            """,
        """
            +------+
            |      |
            |      o
            |      |
            |      |
            |
            ===========
            """,
        """
            +------+
            |      |
            |      o
            |
            |
            |
            ===========
            """,
        """
            +------+
            |      |
            |
            |
            |
            |
            ===========
            """,
    ]
    return stages[tries]


# Exit the Game function
def exit_game():
    """
    Exit game function and explains the player
    how to reset the game back to the beginning
    """

    print(Fore.LIGHTBLUE_EX +
          "Thank you for playing Hangman, come back soon!")
    print(Fore.LIGHTBLUE_EX +
          "To play again please click the Run Program button.")
    sys.exit()


def hangman_game():
    """
    Last function used to call the input name
    and start the hangman.
    """
    input_name()
    start_hangman()

hangman_game()