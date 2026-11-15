import pygame

from settings import (
    GRID_X, GRID_Y,
    TILE_SIZE,
    OFFSET_X, OFFSET_Y
)


class World:

    def __init__(self):

        self.grid = [
            (x, y)
            for x in range(GRID_X)
            for y in range(GRID_Y)
        ]

    def draw_grid(self, surface):

        for tile_x, tile_y in self.grid:

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


def update(self, dt):
    pass
