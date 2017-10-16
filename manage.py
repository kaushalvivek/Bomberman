''' The manage class

# Manage class manages score,
# printing, and the killing of Bomberman.'''


class Manage():
    '''main class to manage scores, lives'''
    score = 0
    lives = 2
    time = 120

    # Function to printthe Header (score, time, lives)
    def printhead(self):
        '''prints the header'''
        print("")
        print("TIME LEFT : " + str(Manage.time))
        print("YOUR SCORE IS : " + str(Manage.score) +
              "\t\t\t\t\t\t      LIVES LEFT : " + str(Manage.lives))
        print("")

    # Function to alter score
    def changescore(self, deleted):
        '''changes the score'''
        if deleted == 'brick':
            Manage.score += 10

        if deleted == 'enemy':
            Manage.score += 100

    # Function to alter lives
    def changelives(self):
        '''changes lives'''
        if Manage.lives == 0:
            print('GAME OVER')
            print('Your Final Score is : ' + str(Manage.score))
            print('')
            quit()
        else:
            Manage.lives -= 1

    # timer for functionality
    def timer(self):
        '''maintains timer'''
        if Manage.time == 0:
            print("Sorry, you ran out of time.")
            print("GAME OVER")
            quit()
        else:
            Manage.time -= 1
