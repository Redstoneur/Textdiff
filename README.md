# Textdiff

---

![License](https://img.shields.io/github/license/Redstoneur/Textdiff)
![Top Language](https://img.shields.io/github/languages/top/Redstoneur/Textdiff)
![Python Version](https://img.shields.io/badge/python-3.13.0-blue)
![Size](https://img.shields.io/github/repo-size/Redstoneur/Textdiff)
![Contributors](https://img.shields.io/github/contributors/Redstoneur/Textdiff)
![Last Commit](https://img.shields.io/github/last-commit/Redstoneur/Textdiff)
![Issues](https://img.shields.io/github/issues/Redstoneur/Textdiff)
![Pull Requests](https://img.shields.io/github/issues-pr/Redstoneur/Textdiff)

---

![Forks](https://img.shields.io/github/forks/Redstoneur/Textdiff)
![Stars](https://img.shields.io/github/stars/Redstoneur/Textdiff)
![Watchers](https://img.shields.io/github/watchers/Redstoneur/Textdiff)

---

![Latest Release](https://img.shields.io/github/v/release/Redstoneur/Textdiff)
![Release Date](https://img.shields.io/github/release-date/Redstoneur/Textdiff)
[![Build Status](https://github.com/Redstoneur/Textdiff/actions/workflows/build.yml/badge.svg)](https://github.com/Redstoneur/Textdiff/actions/workflows/build.yml)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ad771038d4f649f6a6990c204674aebb)](https://app.codacy.com/gh/Redstoneur/Textdiff/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

---

Textdiff is a simple graphical application to compare two texts and visualize their line-by-line differences. It
highlights changes to make proofreading and merging content easier.

## Features

- Intuitive GUI based on Tkinter
- Line-by-line comparison of two texts
- Highlights differences in each text area
- Buttons to compare and clear texts quickly
- Can be run as a Python script or standalone executable (PyInstaller)

## Installation

### Prerequisites

- Python 3.8 or higher (tested up to 3.13)
- `pip` for dependency management

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run unit tests

```bash
python -m unittest discover tests
```

### Run from source

```bash
python main.py
```

### Build an executable (Windows)

Make sure PyInstaller is installed:

```bash
pip install pyinstaller
```

Then build the executable:

```bash
python -m PyInstaller --onefile --windowed --icon=assets/icon.ico --name=Textdiff --add-data "assets/icon.ico;assets" main.py
```

The executable will be available in the `dist/` folder.

## Usage

1. Start the application (`python main.py` or the executable).
2. Paste or type the two texts to compare in the provided areas.
3. Click **Compare** to highlight differences.
4. Click **Clear** to reset the text areas.

Differences are highlighted:

- In red in the left text area
- In green in the right text area

## Development

Main code is in the `testdiff/` folder:

- `textdiffapp.py`: GUI and comparison logic
- `main.py`: application entry point

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
