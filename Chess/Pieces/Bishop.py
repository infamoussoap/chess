from .Piece import Piece
from .utils import algebraic_to_numeric, is_move_diagonal


class Bishop(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Bishop', color)

    def is_valid_move(self, start_pos, end_pos, board):
        end_pos_numeric = algebraic_to_numeric(end_pos)
        board_at_end_pos = board[end_pos_numeric[0], end_pos_numeric[1]]

        if board_at_end_pos.color == self.color:
            return False, "Pieces of the same color cannot capture each other"

        is_diagonal, displacement, diagonally_empty = is_move_diagonal(start_pos, end_pos, board)
        if is_diagonal:
            return Bishop._check_diagonal_move(diagonally_empty)

        return False, "Bishop can only move diagonally"

    @staticmethod
    def _check_diagonal_move(diagonally_empty):
        if not diagonally_empty:
            return False, "There is a piece blocking this move"
        return True, None
