import pygame
from settings import *
from game import *


class World():
    def __init__(self):
        for x in range(GRID_X):
            for y in range(GRID_Y):
                GRID.append((x, y))

    def draw_grid(self):
        for tile_x, tile_y in GRID:

            rect = pygame.Rect(
                OFFSET_X + tile_x * TILE_SIZE,
                OFFSET_Y + tile_y * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )

            pygame.draw.rect(
                surface,
                (100, 100, 100),
                rect,
                1
            )
