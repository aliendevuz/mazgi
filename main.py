from game import Game
from maze import *


maze = beginning_maze()

# game = Game(generate_maze(11, 11))
game = Game(maze)


if __name__ == '__main__':
    game.start()
