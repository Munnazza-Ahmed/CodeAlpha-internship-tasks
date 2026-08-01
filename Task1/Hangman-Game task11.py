"""
CodeAlpha Python Programming Internship
Task 1: Hangman Game (Text-Based)

A simple console-based Hangman game where the player guesses a word
one letter at a time. The player has 6 incorrect guesses before losing.

Key Concepts Used: random, while loop, if-else, strings, lists.
"""

import random

# ------------------------------------------------------------------
# Predefined word list (5 words) — no file or API needed
# ------------------------------------------------------------------
WORDS = ["python", "hangman", "internship", "developer", "keyboard"]

MAX_INCORRECT_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]


def choose_word(word_list):
    """Randomly select a word from the predefined list."""
    return random.choice(word_list).lower()


def display_word(word, guessed_letters):
    """
    Return the word with unguessed letters shown as underscores.
    Example: 'python' with guessed_letters = ['p', 'o'] -> 'p _ _ _ o _'
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_player_guess(guessed_letters):
    """
    Prompt the player for a single valid letter that hasn't been
    guessed yet. Keeps asking until valid input is provided.
    """
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.\n")
        elif not guess.isalpha():
            print("Please enter a valid alphabet letter.\n")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
        else:
            return guess


def play_hangman():
    """Main game loop for a single round of Hangman."""
    word = choose_word(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("=" * 50)
    print("Welcome to HANGMAN!")
    print(f"The word has {len(word)} letters. You have "
          f"{MAX_INCORRECT_GUESSES} incorrect guesses allowed.")
    print("=" * 50)

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses left: "
              f"{MAX_INCORRECT_GUESSES - incorrect_guesses}")

        if guessed_letters:
            print("Letters guessed so far: " + ", ".join(sorted(guessed_letters)))

        guess = get_player_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"\nGood guess! '{guess}' is in the word.\n")
            # Check if the player has won
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_STAGES[incorrect_guesses])
                print(f"Congratulations! You guessed the word: '{word}'")
                print("You WIN! 🎉")
                break
        else:
            incorrect_guesses += 1
            print(f"\nSorry, '{guess}' is not in the word.\n")

    else:
        # This runs only if the while loop completes without 'break'
        # i.e. the player ran out of incorrect guesses
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"You've been hanged! You LOSE. 💀")
        print(f"The word was: '{word}'")


def main():
    """Run the game, allowing the player to play multiple rounds."""
    play_again = "yes"

    while play_again in ("yes", "y"):
        play_hangman()
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

    print("\nThanks for playing Hangman! Goodbye.")


if __name__ == "__main__":
    main()
