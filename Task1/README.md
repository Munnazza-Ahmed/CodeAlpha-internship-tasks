# CodeAlpha_Hangman

A simple, text-based **Hangman** game built in Python as part of the **CodeAlpha Python Programming Internship** (Task 1).

## 📖 About

This is a console-based Hangman game where the player guesses a hidden word one letter at a time. The word is randomly selected from a predefined list, and the player has a limited number of incorrect guesses before the game ends.

## 🎮 How to Play

1. Run the script.
2. A word is randomly chosen from a list of 5 predefined words.
3. Guess the word one letter at a time by typing a single letter and pressing Enter.
4. Correct guesses reveal the letter's position(s) in the word.
5. Incorrect guesses reduce your remaining attempts and draw another part of the hangman.
6. You **win** if you guess all the letters before running out of attempts.
7. You **lose** if you make 6 incorrect guesses — the hangman is fully drawn.
8. After each round, you can choose to play again or exit.

## 🧩 Features

- Randomly selected word from a predefined list of 5 words
- ASCII-art hangman that progressively builds with each wrong guess
- Input validation (rejects empty input, multiple characters, non-letters, and repeated guesses)
- Tracks and displays previously guessed letters
- Replay option to play multiple rounds without restarting the script

## 🛠 Key Concepts Used

- `random` module (word selection)
- `while` loops (game loop)
- `if-else` conditional logic
- String manipulation
- Lists

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Running the Game

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/CodeAlpha_Hangman.git
   cd CodeAlpha_Hangman
   ```
2. Run the script:
   ```bash
   python hangman.py
   ```

## 📂 Project Structure

```
CodeAlpha_Hangman/
│
├── hangman.py      # Main game script
└── README.md        # Project documentation
```

## 🎓 Internship Info

This project was completed as part of the **Python Programming Internship** at [CodeAlpha](https://www.codealpha.tech).

## 📝 License

This project is open-source and free to use for learning purposes.
