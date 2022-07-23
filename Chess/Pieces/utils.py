import numpy as np
from .Blank import Blank


ORDER = np.array(["a", "b", "c", "d", "e", "f", "g", "h"])


def numeric_to_algebraic(pos):
    return ORDER[pos[0]] + str(pos[1] + 1)


def algebraic_to_numeric(pos):
    return (np.argwhere(ORDER == pos[0])[0, 0], int(pos[1]) - 1)


def is_move_vertical(start_pos, end_pos, board):
    """ Positions expected to be in algebraic format """
    start_pos_numeric = algebraic_to_numeric(start_pos)
    end_pos_numeric = algebraic_to_numeric(end_pos)

    if end_pos[0] == start_pos[0]:
        displacement = end_pos_numeric[1] - start_pos_numeric[1]

        vertically_empty = is_empty_vertically(start_pos_numeric, end_pos_numeric, board)

        return True, displacement, vertically_empty

    return False, None, None


def is_empty_vertically(start_pos_numeric, end_pos_numeric, board):
    """ It is assumed that the move is vertical """
    horizontal_pos = start_pos_numeric[0]

    vertical_start = min(start_pos_numeric[1], end_pos_numeric[1])
    vertical_end = max(start_pos_numeric[1], end_pos_numeric[1])

    if vertical_end - vertical_start <= 1:
        return True

    for i in range(vertical_start + 1, vertical_end):
        if not isinstance(board[horizontal_pos, i], Blank):
            return False
    return True


def is_move_horizontal(start_pos, end_pos):
    """ Positions expected to be in algebraic format """
    start_pos_numeric = algebraic_to_numeric(start_pos)
    end_pos_numeric = algebraic_to_numeric(end_pos)

    if end_pos[1] == start_pos[1]:
        displacement = end_pos[0] - start_pos_numeric[0]
        return True, displacement

    return False, None


def is_move_diagonal(start_pos, end_pos):
    start_pos_numeric = algebraic_to_numeric(start_pos)
    end_pos_numeric = algebraic_to_numeric(end_pos)

    displacement = (end_pos_numeric[0] - start_pos_numeric[0], end_pos_numeric[1] - start_pos_numeric[1])

    if abs(displacement[0]) == abs(displacement[1]):
        return True, displacement

    return False, (None, None)
