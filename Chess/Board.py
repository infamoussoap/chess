import numpy as np

from . import Pieces
from .DefaultBoard import default_board


class Board:
    def __init__(self):
        self.board = np.array([[Pieces.Blank() for col in range(8)] for row in range(8)])
        self.move_count = 0

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

    def move(self):
        if self.move_count % 2 == 0:  # White to move
            pass
        else:  # Black to move
            pass

        self.move_count += 1
