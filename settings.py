import pygame

WINDOW_X, WINDOW_Y = 1280, 720

WINDOW = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
pygame.display.set_caption("Satisfactual!")
CLOCK = pygame.time.Clock()
FPS = 60

GRID_X, GRID_Y = 35, 35
TILE_SIZE = 20

OFFSET_X = (WINDOW_X - GRID_X * TILE_SIZE) // 2
OFFSET_Y = (WINDOW_Y - GRID_Y * TILE_SIZE) // 2

# GRID ERSTELLEN
GRID = []

for x in range(GRID_X):
    for y in range(GRID_Y):
        GRID.append((x, y))
