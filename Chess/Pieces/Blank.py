from .Piece import Piece


class Blank(Piece):
    def __init__(self):
        Piece.__init__(self, 'Blank', None)

    @property
    def icon(self):
        return ' '
