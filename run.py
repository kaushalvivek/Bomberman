''' The run file
# Instances of classes created here
# for running the application.'''

import os
from bomberman import Bomberman
from manage import Manage

# TEST is an object of Bomberman
TEST = Bomberman()

# TEST1 is an object of Manage
TEST1 = Manage()

# the initial Welcome Print.
print("")
print("Welcome, to this rendition of Bomberman!")
print("")
print("Press 'Enter' to start playing.")
TAKENINPUT = input()

# This generates bricks on the board
TEST.generatebricks()
# This generates enemies on the board
TEST.generateenemies()
# This generates the bomberman
TEST.generatebomberman()

i = 0
while True:
    os.system("tput reset")
    TEST1.printhead()
    TEST.getprint()

    if i == 10:
        TEST.moveenemies()
        TEST.bombcounter()
        TEST1.timer()
        i = 0
    TEST.movebomberman()
    i = i + 1
