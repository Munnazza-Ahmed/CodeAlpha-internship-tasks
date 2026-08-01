# 🤖 Basic Rule-Based Chatbot

A lightweight, dependency-free command-line chatbot built in pure Python. It uses simple `if-elif-else` logic to map user input to predefined responses — a great beginner project for practicing **functions, conditionals, loops, and user input handling**.

[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-beginner--friendly-brightgreen)](https://docs.python.org/3/tutorial/index.html)

---

## ✨ Features

- 💬 Responds to common greetings (`hello`, `hi`, `hey`)
- 😊 Answers "how are you"
- 🃏 Tells a random programmer joke
- 🙋 Introduces itself when asked its name
- 🙏 Responds to thanks
- 👋 Exits gracefully on `bye`, `quit`, or `exit`
- 🔡 Case-insensitive and whitespace-tolerant input matching
- 🎲 Randomized replies for a more natural feel
- 🛡️ Handles empty input and `Ctrl+C` / `Ctrl+D` gracefully — no crashes

## 📋 Requirements

- Python **3.6+**
- No external libraries needed (uses only the standard library)

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/basic-chatbot.git
cd basic-chatbot
```

### 2. Run the chatbot
```bash
python3 chatbot.py
```

### 3. Chat away!
```
==================================================
 ChatBot: Hello! Type 'bye' or 'quit' to end our chat.
==================================================
You: hello
ChatBot: Hi!
You: how are you
ChatBot: I'm fine, thanks! How about you?
You: tell me a joke
ChatBot: Why do programmers prefer dark mode? Because light attracts bugs!
You: bye
ChatBot: Goodbye!
```

## 🗂️ Project Structure

```
basic-chatbot/
├── chatbot.py    # Main chatbot application
└── README.md     # Project documentation
```

## 🧠 How It Works

The chatbot is built around two core functions:

| Function | Purpose |
|---|---|
| `get_response(user_input)` | Normalizes input and uses `if-elif-else` logic to return a matching reply |
| `is_exit_command(user_input)` | Checks whether the user wants to end the chat |
| `chat()` | Runs the main input/output loop until an exit command is given |

All user input is lowercased and stripped of whitespace before matching, so `"Hello"`, `" hello "`, and `"HELLO"` are all treated the same.

## 🛠️ Extending This Project

Want to build on it? Try:

- Adding more keyword-response rules to `get_response()`
- Loading responses from a JSON or CSV file instead of hardcoding them
- Adding simple NLP (e.g., keyword scoring or `difflib` fuzzy matching)
- Wrapping it in a Flask/Streamlit app for a web-based chat UI
- Logging conversations to a file

## 📄 License

This project is licensed under the MIT License — free to use, modify, and distribute.

## 🙌 Acknowledgements

Built as a beginner Python project to practice core programming fundamentals: functions, conditionals, loops, and user input handling.
