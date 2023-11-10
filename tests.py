# Unit tests for MinesweeperAI class
import unittest
from minesweeper import *


class TestMinesweeperAI(unittest.TestCase):
    def test__addCellsToSentence_allValid(self):
        """
        Test scenario with all neighbors in bound
        """
        ai = MinesweeperAI()
        sentence = Sentence(set(), 0)
        ai._addCellsToSentence(sentence, (4, 5))
        expected = {
            (3, 4),
            (3, 5),
            (3, 6),
            (4, 4),
            (4, 6),
            (5, 4),
            (5, 5),
            (5, 6),
        }
        self.assertEqual(sentence.cells, expected)

    def test__addCellsToSentence_someValid(self):
        """
        Test scenario with some neighbors in bound
        """
        ai = MinesweeperAI()
        sentence = Sentence(set(), 0)
        ai._addCellsToSentence(sentence, (6, 7))
        expected = {
            (5, 6),
            (5, 7),
            (7, 7),
            (7, 6),
            (6, 6),
        }
        self.assertEqual(sentence.cells, expected)


if __name__ == "__main__":
    unittest.main()
