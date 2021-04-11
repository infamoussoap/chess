class unicode_black:
    def __init__(self):
        self.encoding = {'Pawn': '\u265f',
                         'Bishop': '\u265d',
                         'Knight': '\u265e',
                         'Rook': '\u265c',
                         'Queen': '\u265b',
                         'King': '\u265a'}

    def __call__(self, piece_name):
        try:
            return self.encoding[piece_name]
        except KeyError:
            raise ValueError(f'{piece_name} is not a valid name.')


class unicode_white:
    def __init__(self):
        self.encoding = {'Pawn': '\u2659',
                         'Bishop': '\u2657',
                         'Knight': '\u2658',
                         'Rook': '\u2656',
                         'Queen': '\u2655',
                         'King': '\u2654'}

    def __call__(self, piece_name):
        try:
            return self.encoding[piece_name]
        except KeyError:
            raise ValueError(f'{piece_name} is not a valid name.')
