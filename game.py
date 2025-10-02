import pygame
from pygame.locals import *


pygame.init()


size = pygame.display.get_desktop_sizes()[0]


class Game:
    def __init__(self, maze: tuple[list[list[int]]]):
        self.screen = pygame.display.set_mode(size, FULLSCREEN | SCALED)
        self.clock = pygame.time.Clock()
        self.running = True
        print("Game initialized with maze:")
        for side in maze:
            for row in side:
                print(' '.join(str(cell) for cell in row))
            print()

    def start(self):
        print("Game started")
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.stop()

            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        print("Game stopped")
    
    def stop(self):
        self.running = False
