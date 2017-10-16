''' The Check function is an independent
# funciton that returns what is there
# at a specific position.'''

from board import Board


def checkboard(self, alpha, beta):
    ''' checks board for what's at position'''
    if alpha > 18 or beta > 18:
        return 'wall'

    if Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 3] == '/':
        return 'brick'

    if Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 3] == 'E':
        return 'enemy'

    if Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 3] == 'X':
        return 'wall'

    if Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 3] == ' ':
        return 'empty'

    if Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 3] == 'B':
        return 'bomberman'

    if Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 3] == ']':
        return 'bomb'

    if Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 3] == 'e':
        return 'explosion'

    return 'lol'
