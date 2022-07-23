from .Piece import Piece


class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Rook', color)
