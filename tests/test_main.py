import io
import tempfile
import unittest
from contextlib import redirect_stdout

import main


class AlphabetSoupTests(unittest.TestCase):
    def test_find_word_supports_multiple_directions_and_edges(self):
        board = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"],
        ]

        self.assertEqual(main.find_word(board, 3, 3, "ABC"), (0, 0, 0, 2))
        self.assertEqual(main.find_word(board, 3, 3, "CBA"), (0, 2, 0, 0))
        self.assertEqual(main.find_word(board, 3, 3, "ADG"), (0, 0, 2, 0))
        self.assertEqual(main.find_word(board, 3, 3, "AEI"), (0, 0, 2, 2))
        self.assertEqual(main.find_word(board, 3, 3, "CEG"), (0, 2, 2, 0))
        self.assertEqual(main.find_word(board, 3, 3, "I"), (2, 2, 2, 2))

    def test_find_word_handles_missing_and_blank_words(self):
        board = [["A", "B"], ["C", "D"]]
        self.assertIsNone(main.find_word(board, 2, 2, "ZZ"))
        self.assertIsNone(main.find_word(board, 2, 2, "   "))

    def test_solve_outputs_in_input_order_and_skips_not_found(self):
        content = """3x3
A B C
D E F
G H I
ABC
ZZZ
A E I
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = f"{temp_dir}/input.txt"
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

            output = io.StringIO()
            with redirect_stdout(output):
                main.solve(file_path)

        self.assertEqual(output.getvalue().splitlines(), ["ABC 0:0 0:2", "A E I 0:0 2:2"])


if __name__ == "__main__":
    unittest.main()
