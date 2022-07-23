from .Piece import Piece


class Knight(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Knight', color)
