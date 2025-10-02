import pygame
from pygame.locals import *
import time

pygame.init()

size = pygame.display.get_desktop_sizes()[0]
CELL_SIZE = 64  # Har bir katakchaning o'lchami (px)
MARGIN = 32     # Labirintlar orasidagi masofa

# Ranglar
COLORS = {
    ' ': (40, 40, 40),      # devor
    '=': (200, 200, 200),   # yo'l
    '*': (50, 200, 50),     # start
    '#': (200, 50, 50),     # finish
    'o': (50, 50, 200),     # tuynuk
}
PLAYER_COLOR = (255, 255, 0)  # Player sariq rangda

class Game:
    def __init__(self, maze: tuple[list[list[str]], list[list[str]]]):
        self.maze_a, self.maze_b = maze
        self.rows = len(self.maze_a)
        self.cols = len(self.maze_a[0])
        surf_w = self.cols * CELL_SIZE
        surf_h = self.rows * CELL_SIZE
        total_w = surf_w * 2 + MARGIN
        total_h = surf_h
        self.screen = pygame.display.set_mode((total_w, total_h), FULLSCREEN | SCALED)
        self.clock = pygame.time.Clock()
        self.running = True

        self.surf_a = pygame.Surface((surf_w, surf_h))
        self.surf_b = pygame.Surface((surf_w, surf_h))

        self.player_side = 0  # 0 - a, 1 - b
        self.player_pos = self.find_start(self.maze_a)
        self.start_time = None
        self.win = False
        self.elapsed = 0

        self.font = pygame.font.SysFont("consolas", 36)

    def find_start(self, maze):
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == '*':
                    return [x, y]
        return [0, 0]

    def draw_maze(self, surf, maze, player=None):
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                color = COLORS.get(cell, (255, 0, 255))
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(surf, color, rect)
                pygame.draw.rect(surf, (80, 80, 80), rect, 2)
                if player and player[0] == x and player[1] == y:
                    pygame.draw.circle(
                        surf,
                        PLAYER_COLOR,
                        rect.center,
                        CELL_SIZE // 3
                    )

    def can_move(self, side, x, y):
        maze = self.maze_a if side == 0 else self.maze_b
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return maze[y][x] in ('=', '*', '#', 'o')
        return False

    def handle_move(self, dx, dy):
        x, y = self.player_pos
        nx, ny = x + dx, y + dy
        maze = self.maze_a if self.player_side == 0 else self.maze_b
        if self.can_move(self.player_side, nx, ny):
            self.player_pos = [nx, ny]
            # Finish (#) ga yetib keldi
            if maze[ny][nx] == '#':
                self.win = True
                self.elapsed = time.time() - self.start_time

    def can_teleport(self):
        x, y = self.player_pos
        maze = self.maze_a if self.player_side == 0 else self.maze_b
        return maze[y][x] == 'o'

    def teleport(self):
        # Flip side
        prev_side = self.player_side
        self.player_side = 1 - self.player_side
        # Gorizontal flip: x' = cols - 1 - x
        x, y = self.player_pos
        flipped_x = self.cols - 1 - x
        maze = self.maze_a if self.player_side == 0 else self.maze_b
        # Yangi side'dagi o tuynukni shu y satrda topamiz
        for tx in range(self.cols):
            if maze[y][tx] == 'o' and tx == flipped_x:
                self.player_pos = [tx, y]
                return
        for tx in range(self.cols):
            if maze[y][tx] == 'o':
                self.player_pos = [tx, y]
                return

    def draw_win(self):
        msg = f"WIN! Time: {self.elapsed:.2f} s"
        text = self.font.render(msg, True, (255, 255, 255))
        rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, rect)

    def start(self):
        print("Game started")
        self.start_time = time.time()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.stop()
                elif not self.win and event.type == KEYDOWN:
                    if event.key in (K_LEFT, K_a):
                        self.handle_move(-1, 0)
                    elif event.key in (K_RIGHT, K_d):
                        self.handle_move(1, 0)
                    elif event.key in (K_UP, K_w):
                        self.handle_move(0, -1)
                    elif event.key in (K_DOWN, K_s):
                        self.handle_move(0, 1)
                    elif event.key in (K_RETURN, K_SPACE):
                        if self.can_teleport():
                            self.teleport()

            self.surf_a.fill((0, 0, 0))
            self.surf_b.fill((0, 0, 0))
            self.draw_maze(self.surf_a, self.maze_a, self.player_pos if self.player_side == 0 else None)
            self.draw_maze(self.surf_b, self.maze_b, self.player_pos if self.player_side == 1 else None)

            self.screen.fill((20, 20, 20))
            self.screen.blit(self.surf_a, (0, 0))
            self.screen.blit(self.surf_b, (self.surf_a.get_width() + MARGIN, 0))

            # Elapsed time yoki win
            if self.win:
                self.draw_win()
            else:
                elapsed = time.time() - self.start_time
                timer = self.font.render(f"Time: {elapsed:.2f} s", True, (255, 255, 255))
                self.screen.blit(timer, (20, 20))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        print("Game stopped")

    def stop(self):
        self.running = False