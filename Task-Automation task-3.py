#!/usr/bin/env python3
"""
Task Automation with Python Scripts
CodeAlpha Python Programming Internship — Task 3

A small command-line toolkit that automates three common repetitive tasks:

    1. organize   -> Move all .jpg files from a source folder into a destination folder
    2. extract    -> Extract all email addresses from a .txt file into another file
    3. scrape     -> Scrape the <title> of a fixed webpage and save it to a file

Each feature is implemented as an independent, reusable function so any single
one of them can be lifted out and used on its own, while the CLI ties all
three together behind simple subcommands.

Author: (your name here)
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

try:
    import requests
except ImportError:  # requests is only needed for the 'scrape' feature
    requests = None


# --------------------------------------------------------------------------
# Feature 1: Move all .jpg files from one folder to another
# --------------------------------------------------------------------------
def organize_jpg_files(source_dir: str, destination_dir: str) -> int:
    """
    Move every .jpg / .jpeg file found in source_dir into destination_dir.

    Args:
        source_dir: Folder to scan for image files.
        destination_dir: Folder the images will be moved into (created if needed).

    Returns:
        The number of files successfully moved.
    """
    source = Path(source_dir).expanduser().resolve()
    destination = Path(destination_dir).expanduser().resolve()

    if not source.is_dir():
        raise FileNotFoundError(f"Source folder does not exist: {source}")

    destination.mkdir(parents=True, exist_ok=True)

    moved_count = 0
    for file_path in source.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in (".jpg", ".jpeg"):
            target_path = destination / file_path.name

            # Avoid overwriting a file that already exists at the destination
            if target_path.exists():
                stem, suffix = file_path.stem, file_path.suffix
                counter = 1
                while target_path.exists():
                    target_path = destination / f"{stem}_{counter}{suffix}"
                    counter += 1

            shutil.move(str(file_path), str(target_path))
            moved_count += 1
            print(f"Moved: {file_path.name} -> {target_path}")

    print(f"\nDone. {moved_count} .jpg file(s) moved to '{destination}'.")
    return moved_count


# --------------------------------------------------------------------------
# Feature 2: Extract all email addresses from a .txt file
# --------------------------------------------------------------------------
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")


def extract_emails(input_file: str, output_file: str) -> int:
    """
    Find every email address in input_file and write the unique, sorted
    results (one per line) to output_file.

    Args:
        input_file: Path to a .txt file to scan.
        output_file: Path to the .txt file the emails will be written to.

    Returns:
        The number of unique email addresses found.
    """
    input_path = Path(input_file).expanduser().resolve()
    output_path = Path(output_file).expanduser().resolve()

    if not input_path.is_file():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    text = input_path.read_text(encoding="utf-8", errors="ignore")
    emails = sorted(set(EMAIL_PATTERN.findall(text)))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(emails) + ("\n" if emails else ""), encoding="utf-8")

    print(f"Found {len(emails)} unique email address(es).")
    print(f"Saved to: {output_path}")
    return len(emails)


# --------------------------------------------------------------------------
# Feature 3: Scrape the title of a fixed webpage
# --------------------------------------------------------------------------
def scrape_title(url: str, output_file: str) -> str:
    """
    Fetch a webpage and extract the text inside its <title> tag, then save
    it to output_file.

    Args:
        url: The webpage URL to fetch.
        output_file: Path to the .txt file the title will be written to.

    Returns:
        The extracted page title.
    """
    if requests is None:
        raise ImportError(
            "The 'requests' library is required for the scrape feature. "
            "Install it with: pip install requests"
        )

    headers = {"User-Agent": "Mozilla/5.0 (compatible; TaskAutomationBot/1.0)"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    match = re.search(r"<title[^>]*>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
    title = match.group(1).strip() if match else "(No <title> tag found)"
    # Collapse whitespace/newlines that sometimes appear inside <title> tags
    title = " ".join(title.split())

    output_path = Path(output_file).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"URL: {url}\nTitle: {title}\n", encoding="utf-8")

    print(f"Page title: {title}")
    print(f"Saved to: {output_path}")
    return title


# --------------------------------------------------------------------------
# Command-line interface
# --------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="task_automation.py",
        description="Automate small repetitive tasks: organize images, extract emails, or scrape a page title.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # organize
    p_organize = subparsers.add_parser("organize", help="Move all .jpg files into a destination folder")
    p_organize.add_argument("source", help="Folder to scan for .jpg files")
    p_organize.add_argument("destination", help="Folder to move .jpg files into")

    # extract
    p_extract = subparsers.add_parser("extract", help="Extract email addresses from a .txt file")
    p_extract.add_argument("input_file", help="Path to the .txt file to scan")
    p_extract.add_argument(
        "-o", "--output", default="emails_found.txt", help="Output file (default: emails_found.txt)"
    )

    # scrape
    p_scrape = subparsers.add_parser("scrape", help="Scrape the <title> of a webpage")
    p_scrape.add_argument("url", help="URL of the webpage to scrape")
    p_scrape.add_argument(
        "-o", "--output", default="page_title.txt", help="Output file (default: page_title.txt)"
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "organize":
            organize_jpg_files(args.source, args.destination)
        elif args.command == "extract":
            extract_emails(args.input_file, args.output)
        elif args.command == "scrape":
            scrape_title(args.url, args.output)
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()