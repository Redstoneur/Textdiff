"""
Main entry point for the TextDiffApp application.

This script initializes the application, sets the appropriate icon path depending
on the execution context (PyInstaller executable or source code), and starts the
main application loop.
"""

import os
import sys

from testdiff.textdiffapp import TextDiffApp

# Determine the icon path based on the execution context
if hasattr(sys, "_MEIPASS") and getattr(sys, "_MEIPASS"):
    # Running from a PyInstaller executable
    icon_path = os.path.join(getattr(sys, "_MEIPASS"), "assets", "icon.ico")
else:
    # Running from source code
    icon_path = os.path.abspath("./assets/icon.ico")


def main() -> None:
    """
    Initializes and runs the TextDiffApp graphical application.

    This function creates an instance of TextDiffApp with the appropriate icon,
    then starts the application's main event loop.
    """
    # Create an instance of the TextDiffApp graphical application with icons
    app = TextDiffApp(icon_path=icon_path)
    # Start the application's main loop.
    app.run()


if __name__ == "__main__":
    # Entry point of the script
    main()
