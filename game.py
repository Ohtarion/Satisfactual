import pygame
from settings import *
from world import draw_grid


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

    def run(self):
        WINDOW = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
        pygame.display.set_caption("Satisfactual!")
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

            # DISPLAY UPDATE
            pygame.display.flip()

            CLOCK.tick(FPS)

        pygame.quit()


def handle_events(self):
    pass


def update(self, dt):
    pass


def draw(self):
    self.window.fill("black")

    draw_grid(self.window)

    pygame.display.flip()
