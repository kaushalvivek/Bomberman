Welcome to Bomberman!
===================
*Coded by:*
**Vivek Kaushal**

This **README** file contains :
 1.  Information About the Game
 2. Rules of the Game
 3. Description of Classes Created
 4. Instructions on how to Run the Code
 5. Requirements

----------


About The Game
-------------

>**Bomberman** (ボンバーマン Bonbāman, also known as Dyna Blaster in Europe) is a strategic, maze-based video game franchise originally developed by Hudson Soft and currently owned by ***Konami***. The original game was published in 1983 and new games have been published at irregular intervals ever since. Today, Bomberman has featured in over 70 different games on numerous platforms.

For more information click [here](https://en.wikipedia.org/wiki/Bomberman).

----------


Rules of the Game
-------------------

> - You control Bomberman throughout his efforts to climb the 50 floors of the underground labyrinth and reach the surface in order to become human. In order to do this, you must destroy every enemy. (Only a single level implemented in this rendition of the game.)
> - Enemies are undergoing random walk, but *contact* with them can kill your Bomberman.
> - You have 3 lives for your Bomberman, getting killed 3 times will result in a **GAME OVER**.
> - The Bomberman can lay bombs that will kill enemies and destroy bricks in a limited range from where the bomb is planted, the walls remain unaffected. 
> - Destroying each bricks adds 10 points to the score, while killing each enemy adds 100 points.
> - The game lasts for 120 seconds, you have to kill all enemies in that time or you lose.

------------------------

Description of Classes Created
--------------------------------------------
#### Board:
The board class creates a 18x18 board for gameplay, with boundaries, walls and empty spaces. It also comprises of a getprint function to take a print of the board.
#### Bricks:
The Brick class randomly adds 30 bricks to the board in empty spaces. It inherits the Board class.
#### Bomberman:
The Bomberman class has all the variables and functionality of Bomberman, this includes the generation, movement and bomb planting. This inherits Enemy and Bomb.
#### Bomb:
The bomb class does not inherit any other class, it creates a bomb, keeps count of bombs and their positions, explosion, and then clears that explosion.
#### Enemy:
The Enemy class inherits Bricks, and adds 4 enemies to the board, it manages the motion, deletion, generation and functionality of enemies.
#### Manage:
Manage class manages score, printing, and the killing of Bomberman.

__________________

How To Play:
------------------
>- Run the following code to start the game.
```
python3 run.py
```
>- Press enter to start the game.
>- 'w, a, s, d' use these controls for up, left, down, and right.
>- use 'b' to plant a bomb.
>- press 'q' to quit.

___________________

Reqiurements:
--------------------
- Python3

For mac:
```
brew cask update
sudo brew cask install python3
```
For Linux:
```
sudo apt-get update
sudo apt-get install python3
```

_______________

###Vivek Kaushal
####20161071