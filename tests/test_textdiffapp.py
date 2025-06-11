"""
Unit tests for the TextDiffApp class in the testdiff module.
"""

import tkinter as tk
import unittest

from testdiff.textdiffapp import TextDiffApp


class TestTextdiffapp(unittest.TestCase):
    """
    Unit tests for the TextDiffApp class, which provides a GUI for comparing and highlighting
    differences between two text inputs using tkinter.
    """

    def setUp(self):
        """
        Set up a new instance of TextDiffApp before each test and update the GUI.
        """
        self.app = TextDiffApp()
        self.app.update()

    def tearDown(self):
        """
        Destroy the TextDiffApp instance after each test to clean up resources.
        """
        self.app.destroy()

    @staticmethod
    def compare_highlights(widget, tag_name):
        """
        Helper method to retrieve the ranges of text in a widget that are tagged with a specific
        tag.

        :param widget: The tkinter Text widget to check for highlights.
        :param tag_name: The name of the tag to check for.

        :return: A list of tuples containing the start and end indices of highlighted text.
        """
        ranges = widget.tag_ranges(tag_name)
        return [(str(ranges[i]), str(ranges[i + 1])) for i in range(0, len(ranges), 2)]

    def test_empty_texts_no_highlight(self):
        """
        Vérifie qu'aucune surbrillance n'est présente lorsque les deux entrées sont vides.
        """
        self.app.text_a.insert("1.0", "")
        self.app.text_b.insert("1.0", "")
        self.app.compare_texts()
        self.assertEqual(self.compare_highlights(self.app.text_a, "diff"), [])
        self.assertEqual(self.compare_highlights(self.app.text_b, "diff"), [])

    def test_identical_texts_no_highlight(self):
        """
        Vérifie qu'aucune surbrillance n'est présente lorsque les deux entrées sont identiques.
        """
        text = "Ligne 1\nLigne 2\nLigne 3"
        self.app.text_a.insert("1.0", text)
        self.app.text_b.insert("1.0", text)
        self.app.compare_texts()
        self.assertEqual(self.compare_highlights(self.app.text_a, "diff"), [])
        self.assertEqual(self.compare_highlights(self.app.text_b, "diff"), [])

    def test_different_lines_are_highlighted(self):
        """
        Vérifie que les lignes différentes entre les deux entrées sont surlignées.
        """
        self.app.text_a.insert("1.0", "abc\ndef\nghi")
        self.app.text_b.insert("1.0", "abc\nxyz\nghi")
        self.app.compare_texts()
        highlights_a = self.compare_highlights(self.app.text_a, "diff")
        highlights_b = self.compare_highlights(self.app.text_b, "diff")
        self.assertTrue(any("2." in start for start, _ in highlights_a))
        self.assertTrue(any("2." in start for start, _ in highlights_b))

    def test_extra_lines_are_highlighted(self):
        """
        Vérifie que les lignes supplémentaires présentes dans une entrée sont surlignées.
        """
        self.app.text_a.insert("1.0", "a\nb\nc")
        self.app.text_b.insert("1.0", "a\nb\nc\nd")
        self.app.compare_texts()
        highlights_b = self.compare_highlights(self.app.text_b, "diff")
        self.assertTrue(any("4." in start for start, _ in highlights_b))

    def test_clear_texts_removes_highlights(self):
        """
        Vérifie que l'effacement des textes supprime toutes les surbrillances et le contenu.
        """
        self.app.text_a.insert("1.0", "foo\nbar")
        self.app.text_b.insert("1.0", "foo\nbaz")
        self.app.compare_texts()
        self.app.clear_texts()
        self.assertEqual(self.app.text_a.get("1.0", tk.END).strip(), "")
        self.assertEqual(self.app.text_b.get("1.0", tk.END).strip(), "")
        self.assertEqual(self.compare_highlights(self.app.text_a, "diff"), [])
        self.assertEqual(self.compare_highlights(self.app.text_b, "diff"), [])

    def test_unicode_and_empty_lines_handled(self):
        """
        Vérifie que les caractères unicode et les lignes vides sont gérés sans fausse surbrillance.
        """
        self.app.text_a.insert("1.0", "éèà\n\nΩ")
        self.app.text_b.insert("1.0", "éèà\n\nΩ")
        self.app.compare_texts()
        self.assertEqual(self.compare_highlights(self.app.text_a, "diff"), [])
        self.assertEqual(self.compare_highlights(self.app.text_b, "diff"), [])

    def test_whitespace_differences_are_highlighted(self):
        """
        Vérifie que les différences d'espaces sont surlignées.
        """
        self.app.text_a.insert("1.0", "abc def")
        self.app.text_b.insert("1.0", "abc  def")
        self.app.compare_texts()
        highlights_a = self.compare_highlights(self.app.text_a, "diff")
        highlights_b = self.compare_highlights(self.app.text_b, "diff")
        self.assertTrue(highlights_a or highlights_b)


if __name__ == "__main__":
    unittest.main()
