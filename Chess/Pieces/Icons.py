BLACK_PIECES_UNICODE = {'Pawn': '\u265f',
                        'Bishop': '\u265d',
                        'Knight': '\u265e',
                        'Rook': '\u265c',
                        'Queen': '\u265b',
                        'King': '\u265a'}

WHITE_PIECES_UNICODE = {'Pawn': '\u2659',
                        'Bishop': '\u2657',
                        'Knight': '\u2658',
                        'Rook': '\u2656',
                        'Queen': '\u2655',
                        'King': '\u2654'}


def unicode_black(piece_type):
    val = BLACK_PIECES_UNICODE.get(piece_type, None)

    if val is None:
        raise ValueError(f'{piece_name} is not a valid name.')
    return val


def unicode_white(piece_type):
    val = WHITE_PIECES_UNICODE.get(piece_type, None)

    if val is None:
        raise ValueError(f'{piece_name} is not a valid name.')
    return val
