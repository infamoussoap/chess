from .Icons import unicode_black, unicode_white


class Piece:
    def __init__(self, piece_type, color):
        self.piece_type = piece_type
        self.color = color

        self.move_count = 0

    @property
    def icon(self):
        if self.color == 'black':
            return unicode_black(self.piece_type)
        else:
            return unicode_white(self.piece_type)

    @staticmethod
    def is_valid_move(start_pos, end_pos, board):
        """ start_pos and end_pos expected to be in algebraic notation """
        raise NotImplementedError
