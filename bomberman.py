'''The Bomberman class

 The Bomberman class has all the
  variables and functionality of
 Bomberman, this includes the generation,
 movement and bomb planting.
 This inherits Enemy and Bomb.'''

import signal
from enemy import Enemy
from board import Board
from getch import _getChUnix as getChar
from check import checkboard
from alarmexception import AlarmException
from bomb import Bomb
from manage import Manage


class Bomberman(Enemy, Bomb):
    '''main bomberman class'''
    # Coordinates of Bomberman
    bombera = 0
    bomberb = 0

    # Function for the gerneration of Bomberman
    def generatebomberman(self):
        '''generates bomberman'''
        for j in range(0, 4):
            Board.board[2][4 + j] = 'B'
            Board.board[3][4 + j] = 'B'

    # Function for the motion of bomberman as per user input
    def movebomberman(self):
        ''' moves bomberman'''
        def alarmhandler(signum, frame):
            ''' input method '''
            raise AlarmException

        def user_input(timeout=0.1):
            ''' input method '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        char = user_input()

        # Pressing 'i' is a cheat code, that adds extra life.
        if char == 'i':
            Manage.lives += 1

        # Press 'q' for quit.
        if char == 'q':
            quit()

        # Press 'w' for up.
        if char == 'w' and checkboard(self, Bomberman.bombera,
                                      Bomberman.bomberb - 1) == 'empty':
            if checkboard(self, Bomberman.bombera,
                          Bomberman.bomberb) != 'bomb':
                for j in range(0, 4):
                    Board.board[(Bomberman.bomberb + 1) *
                                2][(Bomberman.bombera + 1) * 4 + j] = ' '
                    Board.board[(Bomberman.bomberb + 1) * 2 +
                                1][(Bomberman.bombera + 1) * 4 + j] = ' '

            Bomberman.bomberb = Bomberman.bomberb - 1

            for j in range(0, 4):
                Board.board[(Bomberman.bomberb + 1) *
                            2][(Bomberman.bombera + 1) * 4 + j] = 'B'
                Board.board[(Bomberman.bomberb + 1) * 2 +
                            1][(Bomberman.bombera + 1) * 4 + j] = 'B'

        # Press 's' for down.
        if char == 's' and checkboard(self, Bomberman.bombera,
                                      Bomberman.bomberb + 1) == 'empty':
            if checkboard(self, Bomberman.bombera,
                          Bomberman.bomberb) != 'bomb':
                for j in range(0, 4):
                    Board.board[(Bomberman.bomberb + 1) *
                                2][(Bomberman.bombera + 1) * 4 + j] = ' '
                    Board.board[(Bomberman.bomberb + 1) * 2 +
                                1][(Bomberman.bombera + 1) * 4 + j] = ' '

            Bomberman.bomberb = Bomberman.bomberb + 1

            for j in range(0, 4):
                Board.board[(Bomberman.bomberb + 1) *
                            2][(Bomberman.bombera + 1) * 4 + j] = 'B'
                Board.board[(Bomberman.bomberb + 1) * 2 +
                            1][(Bomberman.bombera + 1) * 4 + j] = 'B'

        # Press 'a' for left.
        if char == 'a' and checkboard(self,
                                      Bomberman.bombera - 1,
                                      Bomberman.bomberb) == 'empty':
            if checkboard(self, Bomberman.bombera,
                          Bomberman.bomberb) != 'bomb':
                for j in range(0, 4):
                    Board.board[(Bomberman.bomberb + 1) *
                                2][(Bomberman.bombera + 1) * 4 + j] = ' '
                    Board.board[(Bomberman.bomberb + 1) * 2 +
                                1][(Bomberman.bombera + 1) * 4 + j] = ' '

            Bomberman.bombera = Bomberman.bombera - 1

            for j in range(0, 4):
                Board.board[(Bomberman.bomberb + 1) *
                            2][(Bomberman.bombera + 1) * 4 + j] = 'B'
                Board.board[(Bomberman.bomberb + 1) * 2 +
                            1][(Bomberman.bombera + 1) * 4 + j] = 'B'

        # Press 'd' for right.
        if char == 'd' and checkboard(self,
                                      Bomberman.bombera + 1,
                                      Bomberman.bomberb) == 'empty':
            if checkboard(self, Bomberman.bombera,
                          Bomberman.bomberb) != 'bomb':
                for j in range(0, 4):
                    Board.board[(Bomberman.bomberb + 1) *
                                2][(Bomberman.bombera + 1) * 4 + j] = ' '
                    Board.board[(Bomberman.bomberb + 1) * 2 +
                                1][(Bomberman.bombera + 1) * 4 + j] = ' '

            Bomberman.bombera = Bomberman.bombera + 1

            for j in range(0, 4):
                Board.board[(Bomberman.bomberb + 1) *
                            2][(Bomberman.bombera + 1) * 4 + j] = 'B'
                Board.board[(Bomberman.bomberb + 1) * 2 +
                            1][(Bomberman.bombera + 1) * 4 + j] = 'B'

        # Press 'b' to plant a bomb.
        if char == 'b':
            self.generatebomb(Bomberman.bombera, Bomberman.bomberb)
