# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# External import statements 
import random
from os import system, name
import sys
from time import sleep
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Import statements I created for the game
from words import english_words
from words import spanish_words
from words import french_words

# Welcome message to Hangman game
def input_name():
    """
    Welcome message and input player name to the console
    """
    print(":::::::::::::::::::::::::::::::::::::")
    print(Fore.GREEN + "           HANGMAN")
    print(Fore.GREEN + "Choose your preferred language and")
    print(Fore.GREEN + "guess the word to win the game!")
    print(":::::::::::::::::::::::::::::::::::::")

    # Print players name with welcome message
    while True:
        player_name = input(Fore.BLUE + "Enter your name here: \n").strip()

        if validate_name(player_name):
            print(f"Hello {player_name} welcome to my game \n")
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
            raise ValueError("\033[0;31mPlease input a name \n")
        elif len(name.strip()) == 0:
            raise ValueError("\033[0;31mPlease input a name \n")
        elif not name.isalpha():
            raise ValueError("error")

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
            break
        elif menu_selection == "2":
            select_language()
            break   
        elif menu_selection == "3":
            exit_game()
            break
        else:
            print("\033[0;31mIncorrect input, please select a valid option from the menu.")

# Instructions explaining how to play the game

def hangman_instructions():
    """
    Game instructions for the player 
    """
    clear()

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
        language = input("\033[0;36mType option 1 for English words, 2 for Spanish words, and 3 for French words: \n")

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
            print("\033[0;31mPlease try again!")

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

        # Request the player to take their turn
        # .upper used to capitalise letters to match the words lists
        start_game = input(
            "\033[0mPlease choose a letter:\n").upper().strip()

        # Clear the terminal
        os.system("cls" if os.name == "nt" else "clear")

        # Test for valid the selection made
        if start_game in guesses:
            print("\033[1;31mOops! You already guessed ", start_game, "\n")
            print("You have used these letters: ")
            print(" ".join(guesses))

        # Accepts one character per guess.
        elif len(start_game) != 1:
            print(
                "\033[1;31mSorry! please only enter one guess at a time\n"
            )
            print("You have used these letters: ")
            print(" ".join(guesses))

        # Makes sure the player guess a letter only.
        elif not start_game.isalpha():
            print("\033[1;31mSorry! ", start_game, " is not a letter\n")
            print("You have used these letters: ")
            print(" ".join(guesses))
        elif start_game not in word:
            print("\033[1;31mPlease try again,", start_game, "is not right")
            attempts -= 1
            print("\033[0mAttempts Remaining: ", attempts)
            guesses.append(start_game)
            print("\033[0mYou have used these letters: ")
            print(" ".join(guesses))
        else:
            print("\033[0;32mGood job! \n")
            guesses.append(start_game)
            print("\033[0mYou have used these letters: ")
            print(" ".join(guesses))
            if start_game in letters:
                letters.remove(start_game)
            else:
                print("\033[0;31mPlease make a valid choice.")

        # Displays no more attempts left.
        if attempts == 0:
            print("\033[0mAttempts Remaining: ", attempts)
            guesses.append(start_game)
            print("\033[0;31mSorry you lose!")

    # Promt the user if he/she want to play again
    print("The correct word was", word, "\n")
    print("\033[0;36mWould you like to try again?")
    play_again()


def play_again():
    """
    Player chooses to play again or exit to the menu.
    """
    while True:
        # try_again only accepts 1 or 2 otherwise an error message is shown.
        try_again = input("Press 1 for Yes or 2 for No: ")

        if try_again == '1':
            select_language()
        elif try_again == '2':
            main_menu()
        else:
            print("\033[0;31mPlease make a valid choice.")
    

# Display the hangman stages

def hangman_status(attempts):
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
    return stages[attempts]

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
    Last function used to call the input_name
    """
    input_name()
    start_hangman()

hangman_game()