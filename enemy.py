''' The Enemy Class

# The Enemy class inherits Bricks,
# and adds 4 enemies to the board,
# it manages the motion, deletion,
# generation and functionality of enemies.'''

from random import randint
from bricks import Bricks
from check import checkboard
from manage import Manage
from board import Board


#   An instance of manage to keep
#   count of time, score and lives.
MANAGEINSTANCE = Manage()


class Enemy(Bricks):
    '''the main Enemy class'''
    # The Coordinates of enemy pushed here.
    aEnemy = []
    bEnemy = []
    Enemies = 4

    # Function to generate enemies.
    def generateenemies(self):
        '''generates enemies'''
        i = 0
        while i < Enemy.Enemies:
            tempa = randint(4, 18)
            tempb = randint(4, 18)
            if tempa % 2 == 1 and tempb % 2 == 1:
                continue

            elif tempa in Bricks.aBricks and tempb in Bricks.bBricks:
                continue

            elif tempa in self.aEnemy and tempb in self.bEnemy:
                continue

            self.aEnemy.append(tempa)
            self.bEnemy.append(tempb)
            i = i + 1

        for i in range(0, Enemy.Enemies):
            tempa = self.aEnemy[i]
            tempb = self.bEnemy[i]

            for j in range(0, Enemy.Enemies):
                Board.board[(tempb + 1) * 2][(tempa + 1) * 4 + j
                                             ] = 'E'

            for j in range(0, Enemy.Enemies):
                Board.board[(tempb + 1) * 2 +
                            1][(tempa + 1) * 4 + j] = 'E'

    # Function for the movement of enemies.
    def moveenemies(self):
        '''moves enemies'''
        for i in range(0, len(self.aEnemy)):

            # flag to check for the death of bomberman
            flag = 0
            tempa = self.aEnemy[i]
            tempb = self.bEnemy[i]
            temp = []
            index = []

            temp.append(checkboard(self, tempa + 1, tempb))
            temp.append(checkboard(self, tempa - 1, tempb))
            temp.append(checkboard(self, tempa, tempb + 1))
            temp.append(checkboard(self, tempa, tempb - 1))

            for j in range(0, 4):
                if temp[j] == 'empty' or temp[j] == 'bomberman':
                    index.append(j)
            vara = len(index)
            if vara == 0:
                continue

            k = randint(0, len(index) - 1)

            if index[k] == 0:
                for j in range(0, 4):
                    Board.board[(tempb + 1) *
                                2][(tempa + 1) * 4 + j] = ' '
                    Board.board[(tempb + 1) * 2 +
                                1][(tempa + 1) * 4 + j] = ' '

                self.aEnemy[i] = self.aEnemy[i] + 1
                tempa = self.aEnemy[i]

                if checkboard(self, tempa, tempb) == 'bomberman':
                    flag = 1

                for j in range(0, 4):
                    Board.board[(tempb + 1) *
                                2][(tempa + 1) * 4 + j] = 'E'
                    Board.board[(tempb + 1) * 2 +
                                1][(tempa + 1) * 4 + j] = 'E'

            elif index[k] == 1:
                for j in range(0, 4):
                    Board.board[(tempb + 1) *
                                2][(tempa + 1) * 4 + j] = ' '
                    Board.board[(tempb + 1) * 2 +
                                1][(tempa + 1) * 4 + j] = ' '

                self.aEnemy[i] = self.aEnemy[i] - 1
                tempa = self.aEnemy[i]

                if checkboard(self, tempa, tempb) == 'bomberman':
                    flag = 1

                for j in range(0, 4):
                    Board.board[(tempb + 1) *
                                2][(tempa + 1) * 4 + j] = 'E'
                    Board.board[(tempb + 1) * 2 +
                                1][(tempa + 1) * 4 + j] = 'E'

            elif index[k] == 2:
                for j in range(0, 4):
                    Board.board[(tempb + 1) *
                                2][(tempa + 1) * 4 + j] = ' '
                    Board.board[(tempb + 1) * 2 +
                                1][(tempa + 1) * 4 + j] = ' '

                self.bEnemy[i] = self.bEnemy[i] + 1
                tempb = self.bEnemy[i]

                if checkboard(self, tempa, tempb) == 'bomberman':
                    flag = 1

                for j in range(0, 4):
                    Board.board[(tempb + 1) *
                                2][(tempa + 1) * 4 + j] = 'E'
                    Board.board[(tempb + 1) * 2 +
                                1][(tempa + 1) * 4 + j] = 'E'

            elif index[k] == 3:
                for j in range(0, 4):
                    Board.board[(tempb + 1) *
                                2][(tempa + 1) * 4 + j] = ' '
                    Board.board[(tempb + 1) * 2 +
                                1][(tempa + 1) * 4 + j] = ' '

                self.bEnemy[i] = self.bEnemy[i] - 1
                tempb = self.bEnemy[i]

                if checkboard(self, tempa, tempb) == 'bomberman':
                    flag = 1

                for j in range(0, 4):
                    Board.board[(tempb + 1) *
                                2][(tempa + 1) * 4 + j] = 'E'
                    Board.board[(tempb + 1) * 2 +
                                1][(tempa + 1) * 4 + j] = 'E'

            if flag:
                flag = 0
                MANAGEINSTANCE.changelives()

    # function for the deletion of enemy
    def removeenemy(self, alpha, beta):
        '''removes enemies'''
        i = 0
        while i < len(self.aEnemy):
            j = 0
            if self.aEnemy[i] == alpha:
                while j < len(self.bEnemy):
                    if self.bEnemy[j] == beta:
                        del self.aEnemy[i]
                        del self.bEnemy[j]
                    j += 1
            i += 1
