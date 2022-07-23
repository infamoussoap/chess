from .Piece import Piece
from .utils import algebraic_to_numeric, is_move_diagonal


class Bishop(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Bishop', color)

    def is_valid_move(self, start_pos, end_pos, board):
        end_pos_numeric = algebraic_to_numeric(end_pos)
        board_at_end_pos = board[end_pos_numeric[0], end_pos_numeric[1]]

        is_diagonal, displacement, diagonally_empty = is_move_diagonal(start_pos, end_pos, board)

        if is_diagonal:
            return diagonally_empty and (board_at_end_pos.color != self.color)

        return False
