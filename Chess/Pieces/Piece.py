from .Representation import unicode_black, unicode_white


class Piece:
    def __init__(self, piece_type, color):
        assert color == 'black' or color == 'white', ValueError(f"{self.color} is invalid type")

        self.piece_type = piece_type
        self.color = color
        self.position = (None, None)

    @property
    def representation(self):
        if self.color == 'black':
            return unicode_black(self.piece_type)
        else:
            return unicode_white(self.piece_type)
