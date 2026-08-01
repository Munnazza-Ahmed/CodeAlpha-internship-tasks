# 📈 Stock Portfolio Tracker

A simple, beginner-friendly Python command-line application that helps users track a stock portfolio, calculate total investment value, and export a summary report — built as part of the **CodeAlpha Python Programming Internship (Task 2)**.

---

## 🚀 Features

- 📋 Displays a list of available stocks with hardcoded, up-to-date prices
- 🧮 Lets users add multiple stocks and quantities interactively
- ➕ Automatically combines duplicate stock entries into a single quantity
- 💰 Calculates per-stock and total investment value
- 🖥️ Clean, tabular console output
- 💾 Optional export of the report to a **`.txt`** or **`.csv`** file
- 🛡️ Input validation — handles invalid symbols, negative numbers, and typos gracefully
- 🔁 No external dependencies — runs with plain Python 3, no `pip install` required

---

## 🧠 Concepts Used

| Concept | Where it's used |
|---|---|
| Dictionaries | Storing stock prices and the user's portfolio |
| Loops (`while`) | Repeated user input until `'done'` |
| Conditionals (`if/elif`) | Input validation |
| Functions | Modular design (build, calculate, display, save) |
| File Handling | Saving reports as `.txt` and `.csv` |
| `csv` module | Structured CSV export |
| f-strings | Formatted console output |

---

## 📦 Requirements

- Python 3.7 or higher
- No external libraries needed (uses only the standard library: `csv`, `datetime`)

---

## ▶️ How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/CodeAlpha_StockPortfolioTracker.git
   cd CodeAlpha_StockPortfolioTracker
   ```

2. **Run the script**
   ```bash
   python stock_portfolio_tracker.py
   ```
   *(On some systems, use `python3` instead of `python`.)*

3. **Follow the prompts:**
   - Enter a stock symbol from the displayed list (e.g. `AAPL`)
   - Enter the quantity you want to "buy"
   - Repeat for as many stocks as you like
   - Type `done` when finished
   - Choose whether to save the report as `txt`, `csv`, or skip saving

---

## 💻 Example Session

```
==================================================
     WELCOME TO THE STOCK PORTFOLIO TRACKER
==================================================

Available Stocks & Prices (USD):
--------------------------------
  AAPL    $180.00
  TSLA    $250.00
  GOOGL   $140.00
  AMZN    $145.00
  MSFT    $310.00
  NFLX    $425.00
  META    $300.00
  NVDA    $460.00
--------------------------------

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity for AAPL: 10
Added: 10 share(s) of AAPL

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity for TSLA: 5
Added: 5 share(s) of TSLA

Enter stock symbol (or 'done' to finish): done

==================================================
           STOCK PORTFOLIO SUMMARY
==================================================
Symbol    Price       Quantity    Total Value
--------------------------------------------------
AAPL      $180.00     10          $1,800.00
TSLA      $250.00     5           $1,250.00
--------------------------------------------------
TOTAL INVESTMENT:                 $3,050.00
==================================================

Would you like to save this report? (txt/csv/no): csv

Report saved successfully to 'portfolio_report.csv'

Thank you for using the Stock Portfolio Tracker. Goodbye!
```

---

## 📁 Project Structure

```
CodeAlpha_StockPortfolioTracker/
│
├── stock_portfolio_tracker.py   # Main application script
├── README.md                    # Project documentation
└── portfolio_report.csv / .txt  # Generated report (created after running the script)
```

---

## 🔧 Customization

Want to add more stocks or change prices? Just edit the `STOCK_PRICES` dictionary at the top of `stock_portfolio_tracker.py`:

```python
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    # Add your own here
    "NEW": 99.99,
}
```

---

## 📜 License

This project was created for educational purposes as part of the **CodeAlpha Python Programming Internship**. Free to use and modify.

---

## 🙌 Acknowledgements

- **CodeAlpha** — for the internship opportunity and project guidelines
- Built with ❤️ using pure Python

---
