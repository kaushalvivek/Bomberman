''' The Brick Class

# The Brick class randomly adds
# 30 bricks to the board in empty
# spaces. It inherits the Board class.'''

from random import randint
from board import Board


class Bricks(Board):
    ''' the main bricks class '''
    # These arrays keep a count
    # of the coordinates of Bricks.
    aBricks = []
    bBricks = []

    # Function to generate Bricks
    def generatebricks(self):
        ''' generates bricks '''
        for i in range(0, 30):
            self.aBricks.append(randint(1, 18))
            self.bBricks.append(randint(1, 18))

        for i in range(0, 30):
            tempa = self.aBricks[i]
            tempb = self.bBricks[i]

            if tempa % 2 == 1 and tempb % 2 == 1:
                continue

            for j in range(0, 4):
                Board.board[(tempb + 1) * 2][(tempa + 1)
                                             * 4 + j] = '/'

            for j in range(0, 4):
                Board.board[(tempb + 1) * 2 +
                            1][(tempa + 1) * 4 + j] = '/'
