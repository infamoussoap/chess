import numpy as np

from .Pieces.utils import algebraic_to_numeric
from . import Pieces
from .DefaultBoard import default_board


class Board:
    def __init__(self):
        self.board = np.array([[Pieces.Blank() for col in range(8)] for row in range(8)])
        self.move_count = 0

        self.move_history = []

    def reset(self):
        self.board = default_board()

    def display(self):
        blank_row = ' ' + '|---'*8 + '|'

        for row in reversed(range(8)):
            print(blank_row)

            pieces_in_row = "".join([f"| {piece.icon} " for piece in self.board[:, row]])
            print(str(row + 1) + pieces_in_row + "|")

        print(blank_row)
        print('   a   b   c   d   e   f   g   h ')

    def move(self, move):
        """ Expected to be in long algebraic notation """

        Board._check_long_algebraic_notation(move)

        start_pos, end_pos = move[:2], move[3:]
        assert not isinstance(self[start_pos], Pieces.Blank), "No piece at starting position"

        if self.move_count % 2 == 0:  # White to move
            assert self[start_pos].color == 'white', "White to move"
        else:  # Black to move
            assert self[start_pos].color == 'black', "Black to move"

        if self[start_pos].is_valid_move(start_pos, end_pos, self):
            self[end_pos] = self[start_pos]
            self[start_pos] = Pieces.Blank()

            self[end_pos].move_count += 1
        else:
            raise ValueError("Invalid Move")

        self.move_count += 1

    @staticmethod
    def _check_long_algebraic_notation(move):
        error_str = "Move expected to be in long algebraic notation, e.g. e2-e4, b1-c3"

        assert len(move) == 5, error_str
        assert move[2] == "-", error_str

        assert ("a" <= move[0] <= "h") and ("a" <= move[3] <= "h"), "Column name out of bounds"
        assert (1 <= int(move[1]) <= 8) and (1 <= int(move[4]) <= 8), "Row name out of bounds"

    def __getitem__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            coords = algebraic_to_numeric(args[0])
            return self.board[coords[0], coords[1]]

        return self.board.__getitem__(*args)

    def __setitem__(self, key, value):
        if isinstance(key, str):
            coords = algebraic_to_numeric(key)
            self.board[coords[0], coords[1]] = value
        else:
            self.board.__setitem__(key, value)
