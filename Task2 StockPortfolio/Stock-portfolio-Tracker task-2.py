"""
Stock Portfolio Tracker
CodeAlpha Python Programming Internship - Task 2

A simple command-line tool that lets a user build a stock portfolio,
calculates the total investment value using hardcoded stock prices,
and optionally saves a summary report to a .txt or .csv file.

Author: (your name here)
"""

import csv
from datetime import datetime

# ----------------------------------------------------------------------
# Hardcoded stock prices (in USD). Feel free to add more tickers here.
# ----------------------------------------------------------------------
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "AMZN": 145.00,
    "MSFT": 310.00,
    "NFLX": 425.00,
    "META": 300.00,
    "NVDA": 460.00,
}


def show_available_stocks():
    """Print the list of stocks and their prices in a neat table."""
    print("\nAvailable Stocks & Prices (USD):")
    print("-" * 32)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8}${price:,.2f}")
    print("-" * 32)


def get_quantity(symbol):
    """
    Ask the user for a quantity for the given stock symbol.
    Keeps asking until a valid non-negative integer is entered.
    """
    while True:
        raw = input(f"Enter quantity for {symbol}: ").strip()
        try:
            qty = int(raw)
            if qty < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
            return qty
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g. 10).")


def build_portfolio():
    """
    Interactively build a portfolio dictionary of {symbol: quantity}
    based on user input. Returns the portfolio dict.
    """
    portfolio = {}
    show_available_stocks()

    print("\nEnter stock symbols to add to your portfolio.")
    print("Type 'done' when you are finished.\n")

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol == "":
            print("Please enter a stock symbol.")
            continue

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in our price list. Please choose from the list above.")
            continue

        qty = get_quantity(symbol)

        if qty == 0:
            print(f"Skipping {symbol} (quantity is 0).")
            continue

        # If the stock is already in the portfolio, add to the existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
        print(f"Added: {qty} share(s) of {symbol}\n")

    return portfolio


def calculate_investment(portfolio):
    """
    Given a portfolio dict {symbol: quantity}, return a list of row dicts
    with symbol, price, quantity, and total value, plus the grand total.
    """
    rows = []
    grand_total = 0.0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        total = price * qty
        grand_total += total
        rows.append({
            "symbol": symbol,
            "price": price,
            "quantity": qty,
            "total": total,
        })

    return rows, grand_total


def display_summary(rows, grand_total):
    """Print a formatted investment summary to the console."""
    if not rows:
        print("\nYour portfolio is empty. Nothing to summarize.")
        return

    print("\n" + "=" * 50)
    print("           STOCK PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Symbol':<10}{'Price':<12}{'Quantity':<12}{'Total Value':<15}")
    print("-" * 50)

    for row in rows:
        print(f"{row['symbol']:<10}${row['price']:<11,.2f}{row['quantity']:<12}${row['total']:<14,.2f}")

    print("-" * 50)
    print(f"{'TOTAL INVESTMENT:':<34}${grand_total:,.2f}")
    print("=" * 50)


def save_to_txt(rows, grand_total, filename="portfolio_report.txt"):
    """Save the portfolio summary to a plain text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n")
        f.write(f"{'Symbol':<10}{'Price':<12}{'Quantity':<12}{'Total Value':<15}\n")
        f.write("-" * 50 + "\n")

        for row in rows:
            f.write(
                f"{row['symbol']:<10}${row['price']:<11,.2f}"
                f"{row['quantity']:<12}${row['total']:<14,.2f}\n"
            )

        f.write("-" * 50 + "\n")
        f.write(f"{'TOTAL INVESTMENT:':<34}${grand_total:,.2f}\n")

    print(f"\nReport saved successfully to '{filename}'")


def save_to_csv(rows, grand_total, filename="portfolio_report.csv"):
    """Save the portfolio summary to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Price (USD)", "Quantity", "Total Value (USD)"])

        for row in rows:
            writer.writerow([row["symbol"], f"{row['price']:.2f}", row["quantity"], f"{row['total']:.2f}"])

        writer.writerow([])
        writer.writerow(["", "", "Total Investment:", f"{grand_total:.2f}"])

    print(f"\nReport saved successfully to '{filename}'")


def handle_save(rows, grand_total):
    """Ask the user if/how they want to save the report, and act accordingly."""
    if not rows:
        return

    choice = input(
        "\nWould you like to save this report? "
        "(txt/csv/no): "
    ).strip().lower()

    if choice == "txt":
        save_to_txt(rows, grand_total)
    elif choice == "csv":
        save_to_csv(rows, grand_total)
    elif choice in ("no", "n", ""):
        print("Report not saved.")
    else:
        print("Unrecognized option. Report not saved.")


def main():
    print("=" * 50)
    print("     WELCOME TO THE STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    portfolio = build_portfolio()
    rows, grand_total = calculate_investment(portfolio)
    display_summary(rows, grand_total)
    handle_save(rows, grand_total)

    print("\nThank you for using the Stock Portfolio Tracker. Goodbye!")


if __name__ == "__main__":
    main()
