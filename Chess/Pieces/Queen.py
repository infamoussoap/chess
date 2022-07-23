from .Piece import Piece


class Queen(Piece):
    def __init__(self, color):
        Piece.__init__(self, 'Queen', color)
