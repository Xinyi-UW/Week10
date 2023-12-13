import unittest
import logic_for_test as logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all functions from logic.py!
    def test_is_board_full(self):
        # Test for is_board_full function
        full_board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
        ]
        self.assertTrue(logic.is_board_full(full_board))

        not_full_board = [
            ['X', 'O', 'X'],
            [None, 'O', 'X'],
            ['O', 'X', 'O'],
        ]
        self.assertFalse(logic.is_board_full(not_full_board))

    def test_is_valid_move(self):
        # Test for is_valid_move function
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertTrue(logic.is_valid_move(board, 0, 1))  # Valid move
        self.assertFalse(logic.is_valid_move(board, 0, 0))  # Invalid move, position already taken

    def test_no_winner(self):
        # Test for get_winner function
        board = [
        ['O', 'O', 'X'],
        ['X', 'X', 'O'],
        ['O', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), None)

if __name__ == '__main__':
    unittest.main()
