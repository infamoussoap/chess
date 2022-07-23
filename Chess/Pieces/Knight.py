from .Piece import Piece
from .utils import algebraic_to_numeric


class Knight(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Knight', color)

    def is_valid_move(self, start_pos, end_pos, board):
        start_pos_numeric = algebraic_to_numeric(start_pos)
        end_pos_numeric = algebraic_to_numeric(end_pos)

        board_at_end_pos = board[end_pos_numeric[0], end_pos_numeric[1]]

        horizontal_displacement = abs(start_pos_numeric[0] - end_pos_numeric[0])
        vertical_displacement = abs(start_pos_numeric[1] - end_pos_numeric[1])

        displacement = [horizontal_displacement, vertical_displacement]

        return (sorted(displacement) == [1, 2]) and (board_at_end_pos.color != self.color)
