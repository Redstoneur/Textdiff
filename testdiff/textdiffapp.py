"""
TextDiffApp module.

This module defines the TextDiffApp class, a Tkinter-based GUI application
for comparing two text inputs and highlighting their differences.
"""

import difflib
import os
import tkinter as tk
from tkinter import ttk
from typing import Optional, List


class TextDiffApp(tk.Tk):
    """
    A graphical application for comparing two text inputs and highlighting their differences.

    Inherits from tk.Tk and provides a user interface with two text areas, comparison and clear
    buttons, and visual highlighting of differing text segments.
    """

    def __init__(self, icon_path: Optional[str] = None) -> None:
        """
        Initialize the TextDiffApp window, set its properties, and create widgets.

        :param icon_path: Optional path to an icon file for the application window.
        """
        super().__init__()
        self.title("Textdiff - Comparateur de texte")
        self.geometry("1000x600")
        self.minsize(800, 400)

        self.icon_path: Optional[str] = (
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

    def create_widgets(self) -> None:
        """
        Create and arrange the main widgets of the application, including text areas and buttons.
        """
        # Utilisation d'un PanedWindow horizontal pour garantir la même largeur
        paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0))

        # Cadre pour la première zone de texte
        frame_a = ttk.Frame(paned)
        self.text_a = tk.Text(frame_a, wrap=tk.WORD, undo=True, font=("Consolas", 12), borderwidth=2, relief="groove")
        self.text_a.pack(fill=tk.BOTH, expand=True)
        paned.add(frame_a, weight=1)

        # Cadre pour la seconde zone de texte
        frame_b = ttk.Frame(paned)
        self.text_b = tk.Text(frame_b, wrap=tk.WORD, undo=True, font=("Consolas", 12), borderwidth=2, relief="groove")
        self.text_b.pack(fill=tk.BOTH, expand=True)
        paned.add(frame_b, weight=1)

        # Cadre pour les boutons, centré
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, pady=15)

        compare_btn = ttk.Button(
            button_frame, text="Comparer", command=self.compare_texts
        )
        clear_btn = ttk.Button(button_frame, text="Effacer", command=self.clear_texts)

        # Centrage des boutons
        button_frame.columnconfigure(0, weight=1)
        compare_btn.grid(row=0, column=1, padx=10)
        clear_btn.grid(row=0, column=2, padx=10)
        button_frame.columnconfigure(3, weight=1)

    def configure_tags(self) -> None:
        """
        Configure text tags for highlighting differences in the text widgets.
        """
        self.text_a.tag_config("diff", background="lightcoral")
        self.text_b.tag_config("diff", background="lightgreen")

    def clear_texts(self) -> None:
        """
        Clear the contents and highlighting of both text widgets.
        """
        for widget in [self.text_a, self.text_b]:
            widget.delete("1.0", tk.END)
            widget.tag_remove("diff", "1.0", tk.END)

    def compare_texts(self) -> None:
        """
        Compare the contents of the two text widgets line by line and highlight differences.
        """
        self.text_a.tag_remove("diff", "1.0", tk.END)
        self.text_b.tag_remove("diff", "1.0", tk.END)

        a_lines: List[str] = self.text_a.get("1.0", tk.END).splitlines()
        b_lines: List[str] = self.text_b.get("1.0", tk.END).splitlines()

        max_lines: int = max(len(a_lines), len(b_lines))

        for i in range(max_lines):
            line_a: str = a_lines[i] if i < len(a_lines) else ""
            line_b: str = b_lines[i] if i < len(b_lines) else ""

            self.highlight_differences(line_a, self.text_a, i + 1, line_b, self.text_b)

    @staticmethod
    def highlight_differences(
            line_a: str,
            widget_a: tk.Text,
            line_num_a: int,
            line_b: str,
            widget_b: tk.Text
    ) -> None:
        """
        Highlight the differences between two lines in their respective text widgets.

        :param line_a: The text from the first widget (Text A).
        :param widget_a: The first text widget (Text A).
        :param line_num_a: The line number of the first widget (Text A).
        :param line_b: The text from the second widget (Text B).
        :param widget_b: The second text widget (Text B).
        """
        sm: difflib.SequenceMatcher = difflib.SequenceMatcher(None, line_a, line_b)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "equal":
                # Text A
                if i2 > i1:
                    start: str = f"{line_num_a}.{i1}"
                    end: str = f"{line_num_a}.{i2}"
                    widget_a.tag_add("diff", start, end)
                # Text B
                if j2 > j1:
                    start: str = f"{line_num_a}.{j1}"
                    end: str = f"{line_num_a}.{j2}"
                    widget_b.tag_add("diff", start, end)

    def run(self) -> None:
        """
        Start the application's main loop.
        This method is called to run the application.
        """
        self.mainloop()


if __name__ == "__main__":
    app: TextDiffApp = TextDiffApp()
    app.run()