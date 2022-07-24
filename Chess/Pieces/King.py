import warnings

from .Piece import Piece
from .utils import algebraic_to_numeric


class King(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'King', color)

    def is_valid_move(self, start_pos, end_pos, board):
        warnings.warn("King needs to check that in the new position the king is not in check")

        start_pos_numeric = algebraic_to_numeric(start_pos)
        end_pos_numeric = algebraic_to_numeric(end_pos)

        board_at_end_pos = board[end_pos_numeric[0], end_pos_numeric[1]]

        if board_at_end_pos.color == self.color:
            return False, "Pieces of the same color cannot capture each other"

        if abs(end_pos_numeric[0] - start_pos_numeric[0]) <= 1\
            and abs(end_pos_numeric[0] - start_pos_numeric[0]) <= 1:
            return True, None

        return False, "Kings can only move in a radius of 1 square around itself"
