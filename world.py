import pygame
from settings import *
from game import *


def draw_grid():
    for tile_x, tile_y in GRID:

        rect = pygame.Rect(
            OFFSET_X + tile_x * TILE_SIZE,
            OFFSET_Y + tile_y * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE
        )

        pygame.draw.rect(
            WINDOW,
            (100, 100, 100),
            rect,
            1
        )
