#!/usr/bin/env python3
"""
Basic Rule-Based Chatbot
=========================
A simple command-line chatbot that maps user input to predefined
responses using if-elif-else conditional logic.

Concepts demonstrated:
    - Functions
    - if-elif-else conditional structures
    - Loops (while)
    - User input handling
    - String normalization (lower/strip) for robust matching

Author: (Your Name)
"""

import random


def get_response(user_input: str) -> str:
    """
    Return a chatbot reply for a given piece of user input.

    Args:
        user_input (str): The raw text typed by the user.

    Returns:
        str: The chatbot's reply.
    """
    # Normalize input: lowercase + strip whitespace so
    # "Hello", " hello ", "HELLO" all match the same rule.
    text = user_input.lower().strip()

    if text == "":
        return "Please say something so I can respond!"

    elif text in ("hello", "hi", "hey", "hi there", "hello there"):
        return random.choice(["Hi!", "Hello there!", "Hey! Nice to see you."])

    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif "your name" in text:
        return "I'm ChatBot, your friendly command-line assistant."

    elif "what can you do" in text or "help" in text:
        return ("I can chat about simple things like greetings, how you're "
                "doing, my name, the time of day, and more. Try me!")

    elif "thank" in text:
        return "You're welcome!"

    elif "joke" in text:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "I would tell you a UDP joke, but you might not get it.",
            "There are 10 types of people: those who understand binary and those who don't."
        ])

    elif "weather" in text:
        return "I can't check live weather, but I hope it's sunny where you are!"

    elif text in ("bye", "goodbye", "exit", "quit", "see you"):
        return "Goodbye!"

    else:
        return "Sorry, I didn't quite understand that. Could you rephrase?"


def is_exit_command(user_input: str) -> bool:
    """
    Determine whether the user wants to end the conversation.

    Args:
        user_input (str): The raw text typed by the user.

    Returns:
        bool: True if the input is an exit/quit command.
    """
    exit_words = ("bye", "goodbye", "exit", "quit", "see you")
    return user_input.lower().strip() in exit_words


def chat() -> None:
    """
    Run the main chatbot loop.

    Continuously prompts the user for input, prints a matching
    response, and stops when an exit command is entered.
    """
    print("=" * 50)
    print(" ChatBot: Hello! Type 'bye' or 'quit' to end our chat.")
    print("=" * 50)

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nChatBot: Goodbye!")
            break

        response = get_response(user_input)
        print(f"ChatBot: {response}")

        if is_exit_command(user_input):
            break


if __name__ == "__main__":
    chat()
