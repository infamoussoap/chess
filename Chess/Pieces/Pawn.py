from .Piece import Piece
from .Blank import Blank
from .utils import algebraic_to_numeric, is_move_vertical, is_move_diagonal


class Pawn(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Pawn', color)
        self.move_count = 0

    def is_valid_move(self, start_pos, end_pos, board):
        start_pos_numeric = algebraic_to_numeric(start_pos)
        end_pos_numeric = algebraic_to_numeric(end_pos)

        board_at_end_pos = board[end_pos_numeric[0], end_pos_numeric[1]]

        end_pos_is_empty = isinstance(board_at_end_pos, Blank)

        # Can only move vertically if end position is empty
        is_vertical, displacement, vertically_empty = is_move_vertical(start_pos, end_pos, board)

        if self.color == 'black':
            displacement = displacement * -1

        if is_vertical:
            if displacement == 1:
                return end_pos_is_empty
            elif displacement == 2:
                return (self.move_count == 0) and end_pos_is_empty and vertically_empty
            return False

        is_diagonal, (_, vertical_displacement) = is_move_diagonal(start_pos, end_pos)

        if self.color == 'black':
            vertical_displacement = vertical_displacement * -1

        if is_diagonal and vertical_displacement == 1:
            return (not end_pos_is_empty) and (board_at_end_pos.color != self.color)

        return False
