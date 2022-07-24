from .Piece import Piece
from .Blank import Blank
from .utils import algebraic_to_numeric, is_move_vertical, is_move_diagonal


class Pawn(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Pawn', color)

    def is_valid_move(self, start_pos, end_pos, board):
        start_pos_numeric = algebraic_to_numeric(start_pos)
        end_pos_numeric = algebraic_to_numeric(end_pos)

        board_at_end_pos = board[end_pos_numeric[0], end_pos_numeric[1]]

        end_pos_is_empty = isinstance(board_at_end_pos, Blank)

        if board_at_end_pos.color == self.color:
            return False, "Pieces of the same color cannot capture each other"

        # Can only move vertically if end position is empty
        is_vertical, displacement, vertically_empty = is_move_vertical(start_pos, end_pos, board)
        if is_vertical:
            if self.color == 'black':
                displacement = displacement * -1

            return Pawn._check_vertical_move(displacement, end_pos_is_empty, vertically_empty, self.move_count)

        is_diagonal, (_, vertical_displacement), _ = is_move_diagonal(start_pos, end_pos, board)
        if is_diagonal:
            if self.color == 'black':
                vertical_displacement = vertical_displacement * -1
            return Pawn._check_diagonal_move(vertical_displacement, end_pos_is_empty)

        return False, "Pawn can only move vertically or diagonally"

    @staticmethod
    def _check_vertical_move(displacement, end_pos_is_empty, vertically_empty, move_count):
        if displacement < 0:
            return False, "Pawn cannot move backwards"
        elif displacement > 2:
            return False, "Pawn cannot move more than 2 squares vertically"
        elif not end_pos_is_empty:
            return False, "Pawn can only move vertically if the end square is empty"
        elif displacement == 2 and move_count != 0:
            return False, "Pawn can only move 2 squares vertically if the pawn hasn't moved"
        elif displacement == 2 and move_count == 0 and not vertically_empty:
            return False, "There is a piece blocking this move"

        return True, None

    @staticmethod
    def _check_diagonal_move(vertical_displacement, end_pos_is_empty):
        if vertical_displacement < 0:
            return False, "Pawn cannot move backwards"
        elif vertical_displacement > 1:
            return False, "Pawn can only move 1 square diagonally"
        elif end_pos_is_empty:
            return False, "Pawn can only move diagonally if the square is not empty"

        return True, None
