import pygame
from settings import *


class Game:
    def __init__(self):
        pass

    def run(self):
        running = True
        while running:

            # EVENTS
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            WINDOW = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
            pygame.display.set_caption("Satisfactual!")
            # BACKGROUND
            WINDOW.fill("Black")

            for x in range(GRID_X):
                for y in range(GRID_Y):
                    GRID.append((x, y))

            # DISPLAY UPDATE
            pygame.display.flip()

            CLOCK.tick(FPS)

        pygame.quit()


def handle_events(self):
    pass


def update(self, dt):
    pass


def draw(self):
    pass
