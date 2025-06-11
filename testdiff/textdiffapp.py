"""
TextDiffApp module.

This module defines the TextDiffApp class, a Tkinter-based GUI application
for comparing two text inputs and highlighting their differences.
"""

import difflib
import os
import tkinter as tk
from tkinter import ttk


class TextDiffApp(tk.Tk):
    """
    A graphical application for comparing two text inputs and highlighting their differences.

    Inherits from tk.Tk and provides a user interface with two text areas, comparison and clear buttons,
    and visual highlighting of differing text segments.
    """

    def __init__(self, icon_path=None) -> None:
        """
        Initialize the TextDiffApp window, set its properties, and create widgets.

        :param icon_path: Optional path to an icon file for the application window.
        """
        super().__init__()
        self.title("Textdiff - Comparateur de texte")
        self.geometry("1000x600")
        self.minsize(800, 400)

        self.icon_path: str | None = (
            os.path.abspath(icon_path) if icon_path else None
        )
        self.set_icon()

        self.create_widgets()
        self.configure_tags()

    def set_icon(self) -> None:
        """
        Set the application icon if the icon path is valid.

        This method is called during initialization to set the window icon.
        """
        if self.icon_path and os.path.exists(self.icon_path):
            try:
                self.iconbitmap(self.icon_path)
            except tk.TclError:
                pass

    def create_widgets(self):
        """
        Create and arrange the main widgets of the application, including text areas and buttons.
        """
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        self.text_a = tk.Text(frame, wrap=tk.WORD, undo=True)
        self.text_b = tk.Text(frame, wrap=tk.WORD, undo=True)

        self.text_a.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.text_b.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))

        button_frame = ttk.Frame(self, padding=10)
        button_frame.pack(fill=tk.X)

        compare_btn = ttk.Button(button_frame, text="Comparer", command=self.compare_texts)
        clear_btn = ttk.Button(button_frame, text="Effacer", command=self.clear_texts)

        compare_btn.pack(side=tk.LEFT, padx=5)
        clear_btn.pack(side=tk.LEFT, padx=5)

    def configure_tags(self):
        """
        Configure text tags for highlighting differences in the text widgets.
        """
        self.text_a.tag_config("diff", background="lightcoral")
        self.text_b.tag_config("diff", background="lightgreen")

    def clear_texts(self):
        """
        Clear the contents and highlighting of both text widgets.
        """
        for widget in [self.text_a, self.text_b]:
            widget.delete("1.0", tk.END)
            widget.tag_remove("diff", "1.0", tk.END)

    def compare_texts(self):
        """
        Compare the contents of the two text widgets line by line and highlight differences.
        """
        self.text_a.tag_remove("diff", "1.0", tk.END)
        self.text_b.tag_remove("diff", "1.0", tk.END)

        a_lines = self.text_a.get("1.0", tk.END).splitlines()
        b_lines = self.text_b.get("1.0", tk.END).splitlines()

        max_lines = max(len(a_lines), len(b_lines))

        for i in range(max_lines):
            line_a = a_lines[i] if i < len(a_lines) else ""
            line_b = b_lines[i] if i < len(b_lines) else ""

            self.highlight_differences(line_a, self.text_a, i + 1, line_b, self.text_b)

    @staticmethod
    def highlight_differences(line_a, widget_a, line_num_a, line_b, widget_b):
        """
        Highlight the differences between two lines in their respective text widgets.

        :param line_a: The text from the first widget (Text A).
        :param widget_a: The first text widget (Text A).
        :param line_num_a: The line number of the first widget (Text A).
        :param line_b: The text from the second widget (Text B).
        :param widget_b: The second text widget (Text B).
        """
        sm = difflib.SequenceMatcher(None, line_a, line_b)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "equal":
                # Text A
                if i2 > i1:
                    start = f"{line_num_a}.{i1}"
                    end = f"{line_num_a}.{i2}"
                    widget_a.tag_add("diff", start, end)
                # Text B
                if j2 > j1:
                    start = f"{line_num_a}.{j1}"
                    end = f"{line_num_a}.{j2}"
                    widget_b.tag_add("diff", start, end)

    def run(self):
        """
        Start the application's main loop.
        This method is called to run the application.
        """
        self.mainloop()


if __name__ == "__main__":
    app = TextDiffApp()
    app.run()