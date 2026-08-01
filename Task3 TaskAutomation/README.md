# CodeAlpha_TaskAutomation

**Python Programming Internship — CodeAlpha**
**Task 3: Task Automation with Python Scripts**

A single, well-tested command-line toolkit that automates three common repetitive tasks — all in one script, selectable via subcommands. Built to run out of the box on Windows, macOS, or Linux with only the standard library plus `requests`.

## ✨ Features

| Subcommand | What it does | Concepts used |
|---|---|---|
| `organize` | Moves every `.jpg` / `.jpeg` file from a source folder into a destination folder (auto-renames on name clashes) | `os`, `shutil`, `pathlib` |
| `extract` | Scans a `.txt` file and extracts every unique email address into a new file | `re`, file handling |
| `scrape` | Fetches a webpage and saves its `<title>` to a file | `requests`, `re` |

Each feature is written as a standalone, reusable Python function (`organize_jpg_files`, `extract_emails`, `scrape_title`), so you can import and use any one of them independently of the CLI.

## 📦 Requirements

- Python 3.7+
- `requests` (only needed for the `scrape` command)

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🖥 Running in VS Code

This folder is a ready-to-open VS Code project:

1. Open the folder in VS Code: **File → Open Folder** → select `CodeAlpha_TaskAutomation`.
2. Install the **Python** extension (by Microsoft) if you don't already have it.
3. Select a Python interpreter: **Ctrl/Cmd+Shift+P → "Python: Select Interpreter"**.
4. Install dependencies in the integrated terminal: `pip install -r requirements.txt`.
5. Open the **Run and Debug** panel (`Ctrl/Cmd+Shift+D`), pick one of the three pre-configured run profiles from the dropdown, then press ▶️:
   - **Organize: Move .jpg files** — uses the included `test_src/` sample folder
   - **Extract: Emails from .txt** — uses the included `sample.txt`
   - **Scrape: Webpage title** — scrapes `https://www.example.com`

You can also just run any command directly in the integrated terminal — see [Usage](#-usage) below.

## 🚀 Usage

### 1. Organize — move all `.jpg` files into a folder

```bash
python task_automation.py organize <source_folder> <destination_folder>
```

Example:

```bash
python task_automation.py organize ./Downloads ./Photos
```

### 2. Extract — pull email addresses out of a text file

```bash
python task_automation.py extract <input_file.txt> -o <output_file.txt>
```

Example:

```bash
python task_automation.py extract contacts.txt -o emails_found.txt
```

If `-o` is omitted, results are saved to `emails_found.txt` by default.

### 3. Scrape — save a webpage's title

```bash
python task_automation.py scrape <url> -o <output_file.txt>
```

Example:

```bash
python task_automation.py scrape https://www.example.com -o page_title.txt
```

If `-o` is omitted, results are saved to `page_title.txt` by default.

### Help

Every command supports `-h` for details:

```bash
python task_automation.py -h
python task_automation.py organize -h
python task_automation.py extract -h
python task_automation.py scrape -h
```

## 🧠 How It Works (Quick Overview)

- **`organize_jpg_files()`** walks a source directory with `pathlib`, filters by file extension, and uses `shutil.move()` to relocate matches, generating a safe alternate filename if a collision is detected at the destination.
- **`extract_emails()`** reads the target file as text and applies a regex pattern to capture standard email formats, then de-duplicates and sorts the results before writing them out.
- **`scrape_title()`** sends an HTTP GET request with a browser-like `User-Agent` header, then uses a regex to pull the contents of the `<title>` tag out of the raw HTML response.

## 🛡 Error Handling

The script validates inputs up front (missing folders/files, failed HTTP requests, missing dependencies) and prints clear error messages to `stderr` instead of crashing with a raw traceback.

## 📁 Project Structure

```
CodeAlpha_TaskAutomation/
├── .vscode/
│   ├── launch.json        # Pre-configured VS Code run/debug profiles
│   └── settings.json      # Workspace settings
├── test_src/               # Sample .jpg files for the 'organize' demo
├── sample.txt               # Sample text file for the 'extract' demo
├── task_automation.py    # Main script (all three features + CLI)
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md               # This file
```

## 🎓 About

This project was built as part of the **CodeAlpha Python Programming Internship**, Task 3 — *Task Automation with Python Scripts*.

## 📄 License

This project is open source and available for learning purposes.
