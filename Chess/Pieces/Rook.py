from .Piece import Piece
from .utils import algebraic_to_numeric, is_move_vertical, is_move_horizontal

class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Rook', color)

    def is_valid_move(self, start_pos, end_pos, board):
        is_vertical, displacement, vertically_empty = is_move_vertical(start_pos, end_pos, board)
        if is_vertical:
            return vertically_empty

        is_horizontal, displacement, horizontally_empty = is_move_horizontal(start_pos, end_pos, board)
        if is_horizontal:
            return horizontally_empty

        return False
