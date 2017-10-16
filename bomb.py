'''   The Bomb Class

 The bomb class does not inherit
 any other class, it creates a bomb,
 keeps count of bombs and their positions,
 explosion, and then clears that explosion.
'''

from check import checkboard
from board import Board
from enemy import Enemy
from manage import Manage

#   An instance of manage to keep
#   count of time, score and lives.
MANAGEINSTANCE = Manage()


class Bomb:
    '''Bomb class has all bomb functions.'''
    # Arrays for x,y coordinates of Bombs
    Bomba = []
    Bombb = []

    # the explosion function to explode bombs.
    # Dealt individually for 4 positions around a coordinate.
    def explosion(self, alpha, beta):
        '''Deals with explosion of bomb'''
        # For the oroginal position.
        for j in range(0, 4):
            Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
            Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        beta = beta - 1

        # For down.
        if checkboard(self, alpha, beta) == 'enemy':
            MANAGEINSTANCE.changescore('enemy')
            Enemy.removeenemy(self, alpha, beta)
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'empty':
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'bomberman':
            MANAGEINSTANCE.changelives()
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'bomb':
            self.removebomb(alpha, beta)
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'brick':
            MANAGEINSTANCE.changescore('brick')
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        alpha = alpha + 1
        beta = beta + 1

        # For Right
        if checkboard(self, alpha, beta) == 'enemy':
            MANAGEINSTANCE.changescore('enemy')
            Enemy.removeenemy(self, alpha, beta)
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'empty':
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'bomberman':
            MANAGEINSTANCE.changelives()
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'bomb':
            self.removebomb(alpha, beta)
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'brick':
            MANAGEINSTANCE.changescore('brick')
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        alpha = alpha - 2

        # For Left
        if checkboard(self, alpha, beta) == 'enemy':
            MANAGEINSTANCE.changescore('enemy')
            Enemy.removeenemy(self, alpha, beta)
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'empty':
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'bomberman':
            MANAGEINSTANCE.changelives()
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'bomb':
            self.removebomb(alpha, beta)
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'brick':
            MANAGEINSTANCE.changescore('brick')
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        alpha = alpha + 1
        beta = beta + 1

        # For Down
        if checkboard(self, alpha, beta) == 'enemy':
            MANAGEINSTANCE.changescore('enemy')
            Enemy.removeenemy(self, alpha, beta)
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'empty':
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'bomberman':
            MANAGEINSTANCE.changelives()
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'bomb':
            self.removebomb(alpha, beta)
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        if checkboard(self, alpha, beta) == 'brick':
            MANAGEINSTANCE.changescore('brick')
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = 'e'
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = 'e'

        beta = beta - 1

    # Function to clear explosion after an
    # explosion has lasted for 10 frames.
    def clearexplosion(self, alpha, beta):
        '''clears bomb explosion'''
        for j in range(0, 4):
            Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = ' '
            Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = ' '

        beta = beta - 1

        if checkboard(self, alpha, beta) == 'explosion':
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = ' '
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = ' '

        alpha = alpha + 1
        beta = beta + 1

        if checkboard(self, alpha, beta) == 'explosion':
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = ' '
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = ' '

        alpha = alpha - 2

        if checkboard(self, alpha, beta) == 'explosion':
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = ' '
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = ' '

        alpha = alpha + 1
        beta = beta + 1

        if checkboard(self, alpha, beta) == 'explosion':
            for j in range(0, 4):
                Board.board[(beta + 1) * 2][(alpha + 1) * 4 + j] = ' '
                Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + j] = ' '

        beta = beta - 1
        self.removebomb(alpha, beta)

    # Once an explosion has been cleared
    # The removebomb function removes those
    # bomb coordinates from the bomb array.
    def removebomb(self, alpha, beta):
        '''removes bomb from bomb array'''
        i = 0
        while i < len(self.Bomba):
            j = 0
            if self.Bomba[i] == alpha:
                while j < len(self.Bombb):
                    if self.Bombb[j] == beta:
                        del self.Bomba[i]
                        del self.Bombb[j]
                    j += 1
            i += 1

    # The bombcounter funciton displays
    # Seconds to explosion at bomb coordinates.
    def bombcounter(self):
        '''keeps a count of number of bombs'''
        i = 0
        while i < len(Bomb.Bomba):
            if Board.board[(Bomb.Bombb[i] + 1) * 2 +
                           1][(Bomb.Bomba[i] + 1) * 4 + 2] == '2':
                Board.board[(Bomb.Bombb[i] + 1) * 2 +
                            1][(Bomb.Bomba[i] + 1) * 4 + 2] = '1'
                Board.board[(Bomb.Bombb[i] + 1) * 2 +
                            1][(Bomb.Bomba[i] + 1) * 4 + 1] = '1'
                Board.board[(Bomb.Bombb[i] + 1) *
                            2][(Bomb.Bomba[i] + 1) * 4 + 2] = '1'
                Board.board[(Bomb.Bombb[i] + 1) *
                            2][(Bomb.Bomba[i] + 1) * 4 + 1] = '1'

            elif Board.board[(Bomb.Bombb[i] + 1) * 2 + 1][(Bomb.Bomba[i] + 1) * 4 + 2] == '1':
                Board.board[(Bomb.Bombb[i] + 1) * 2 +
                            1][(Bomb.Bomba[i] + 1) * 4 + 2] = '0'
                Board.board[(Bomb.Bombb[i] + 1) * 2 +
                            1][(Bomb.Bomba[i] + 1) * 4 + 1] = '0'
                Board.board[(Bomb.Bombb[i] + 1) *
                            2][(Bomb.Bomba[i] + 1) * 4 + 2] = '0'
                Board.board[(Bomb.Bombb[i] + 1) *
                            2][(Bomb.Bomba[i] + 1) * 4 + 1] = '0'

            elif Board.board[(Bomb.Bombb[i] + 1) * 2 + 1][(Bomb.Bomba[i] + 1) * 4 + 2] == '0':
                Bomb.explosion(self, Bomb.Bomba[i], Bomb.Bombb[i])

            elif Board.board[(Bomb.Bombb[i] + 1) * 2 + 1][(Bomb.Bomba[i] + 1) * 4 + 2] == 'e':
                Bomb.clearexplosion(
                    self, Bomb.Bomba[i], Bomb.Bombb[i])
            i += 1

    # Function to generate bombs.
    def generatebomb(self, alpha, beta):
        '''generates bombs'''
        Bomb.Bomba.append(alpha)
        Bomb.Bombb.append(beta)
        Board.board[(beta + 1) * 2][(alpha + 1) * 4] = '['
        Board.board[(beta + 1) * 2][(alpha + 1) * 4 + 1] = '2'
        Board.board[(beta + 1) * 2][(alpha + 1) * 4 + 2] = '2'
        Board.board[(beta + 1) * 2][(alpha + 1) * 4 + 3] = ']'
        Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4] = '['
        Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 1] = '2'
        Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 2] = '2'
        Board.board[(beta + 1) * 2 + 1][(alpha + 1) * 4 + 3] = ']'
