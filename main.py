from game import Game
from maze import *


maze = sample_maze()

game = Game(maze)


if __name__ == '__main__':
    game.start()
