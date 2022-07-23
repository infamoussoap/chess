import numpy as np

from . import Pieces


def default_board():
    board = np.array([[Pieces.Blank() for col in range(8)] for row in range(8)])

    set_rooks(board)
    set_knights(board)
    set_bishops(board)
    set_queen_and_king(board)
    set_pawns(board)

    return board

def set_rooks(board):
    board[0, 0] = Pieces.Rook('white')
    board[0, 7] = Pieces.Rook('white')
    board[7, 0] = Pieces.Rook('black')
    board[7, 7] = Pieces.Rook('black')

def set_knights(board):
    board[0, 1] = Pieces.Knight('white')
    board[0, 6] = Pieces.Knight('white')
    board[7, 1] = Pieces.Knight('black')
    board[7, 6] = Pieces.Knight('black')

def set_bishops(board):
    board[0, 2] = Pieces.Bishop('white')
    board[0, 5] = Pieces.Bishop('white')
    board[7, 2] = Pieces.Bishop('black')
    board[7, 5] = Pieces.Bishop('black')

def set_queen_and_king(board):
    board[0, 3] = Pieces.Queen('white')
    board[0, 4] = Pieces.King('white')
    board[7, 3] = Pieces.Queen('black')
    board[7, 4] = Pieces.King('black')

def set_pawns(board):
    for i in range(8):
        board[1, i] = Pieces.Pawn('white')
        board[6, i] = Pieces.Pawn('black')
