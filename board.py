''' The Board Class :
The board class creates a 18x18 board for gameplay,
with boundaries, walls and empty spaces. It also
comprises of a getprint function to take a print
of the board.'''


class Board:
    '''The main board class'''
    board = [[] for i in range(0, 42)]

    # Types of Rows
    boundaryWalls = ["X" for i in range(0, 84)]
    normalRow = []
    normalRowWithBricks = []

    for i in range(0, 84):
        if i < 4 or i >= 80:
            normalRow.append('X')
        else:
            normalRow.append(' ')

    for i in range(0, 84):
        if i >= 80:
            normalRowWithBricks.append('X')
        elif i % 8 < 4:
            if i < 80:
                normalRowWithBricks.append('X')
        else:
            if i < 80:
                normalRowWithBricks.append(' ')

    for i in range(0, 42):
        if i < 2 or i >= 40:
            board[i] = boundaryWalls[:]
        elif (i - 2) % 4 < 2:
            board[i] = normalRow[:]
        else:
            board[i] = normalRowWithBricks[:]

    # The Basic Function to get a print of the board.
    def getprint(self):
        '''Method to get a print of board'''
        temp = ['' for i in range(0, 84)]

        for j in range(0, 42):
            for i in range(0, 84):
                temp[j] = temp[j] + self.board[j][i]

        for i in range(0, 42):
            print(temp[i])
