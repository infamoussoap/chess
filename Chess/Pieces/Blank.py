from .Piece import Piece


class Blank(Piece):
    def __init__(self):
        Piece.__init__(self, 'Blank', None)

    @property
    def icon(self):
        return ' '

    def is_valid_move(self, start_pos, end_pos, board):
        raise ValueError("Blank Piece cannot move")
