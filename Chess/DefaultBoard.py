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
    board[7, 0] = Pieces.Rook('white')
    board[0, 7] = Pieces.Rook('black')
    board[7, 7] = Pieces.Rook('black')

def set_knights(board):
    board[1, 0] = Pieces.Knight('white')
    board[6, 0] = Pieces.Knight('white')
    board[1, 7] = Pieces.Knight('black')
    board[6, 7] = Pieces.Knight('black')

def set_bishops(board):
    board[2, 0] = Pieces.Bishop('white')
    board[5, 0] = Pieces.Bishop('white')
    board[2, 7] = Pieces.Bishop('black')
    board[5, 7] = Pieces.Bishop('black')

def set_queen_and_king(board):
    board[3, 0] = Pieces.Queen('white')
    board[4, 0] = Pieces.King('white')
    board[3, 7] = Pieces.Queen('black')
    board[4, 7] = Pieces.King('black')

def set_pawns(board):
    for i in range(8):
        board[i, 1] = Pieces.Pawn('white')
        board[i, 6] = Pieces.Pawn('black')
