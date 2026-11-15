import pygame
from settings import *

running = True
while running:

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # BACKGROUND
    WINDOW.fill("Black")

    # GRID ZEICHNEN
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

    # DISPLAY UPDATE
    pygame.display.flip()

    CLOCK.tick(FPS)

pygame.quit()
