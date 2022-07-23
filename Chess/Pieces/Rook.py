from .Piece import Piece
from .utils import algebraic_to_numeric, is_move_vertical, is_move_horizontal

class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Rook', color)

    def is_valid_move(self, start_pos, end_pos, board):
        end_pos_numeric = algebraic_to_numeric(end_pos)
        board_at_end_pos = board[end_pos_numeric[0], end_pos_numeric[1]]

        is_vertical, displacement, vertically_empty = is_move_vertical(start_pos, end_pos, board)
        if is_vertical:
            return vertically_empty and (board_at_end_pos.color != self.color)

        is_horizontal, displacement, horizontally_empty = is_move_horizontal(start_pos, end_pos, board)
        if is_horizontal:
            return horizontally_empty and (board_at_end_pos.color != self.color)

        return False
