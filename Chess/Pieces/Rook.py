from .Piece import Piece
from .utils import algebraic_to_numeric, is_move_vertical, is_move_horizontal


class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Rook', color)

    def is_valid_move(self, start_pos, end_pos, board):
        end_pos_numeric = algebraic_to_numeric(end_pos)
        board_at_end_pos = board[end_pos_numeric[0], end_pos_numeric[1]]

        if board_at_end_pos.color == self.color:
            return False, "Pieces of the same color cannot capture each other"

        is_vertical, displacement, vertically_empty = is_move_vertical(start_pos, end_pos, board)
        if is_vertical:
            return Rook._check_vertical_move(vertically_empty)

        is_horizontal, displacement, horizontally_empty = is_move_horizontal(start_pos, end_pos, board)
        if is_horizontal:
            return Rook._check_horizontal_move(horizontally_empty)

        return False, "Rook can only move vertically or horizontally"

    @staticmethod
    def _check_vertical_move(vertically_empty):
        if not vertically_empty:
            return False, "There is a piece blocking this move"
        return True, None

    @staticmethod
    def _check_horizontal_move(horizontally_empty):
        if not horizontally_empty:
            return False, "There is a piece blocking this move"
        return True, None
