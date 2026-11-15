import pygame

from settings import *
from world import World


class Game:

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode(
            (WINDOW_X, WINDOW_Y)
        )

        pygame.display.set_caption("Satisfactual!")

        self.clock = pygame.time.Clock()
        self.running = True

        self.world = World()

    def run(self):

        while self.running:

            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(FPS)

        pygame.quit()

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        pass

    def draw(self):

        self.window.fill(BACKGROUND_COLOR)

        self.world.draw_grid(self.window)

        pygame.display.flip()
