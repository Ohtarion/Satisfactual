import pygame

pygame.init()

WINDOW_X, WINDOW_Y = 1280, 720

WINDOW = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
pygame.display.set_caption("Satisfactual!")

CLOCK = pygame.time.Clock()
FPS = 60

GRID_X, GRID_Y = 35, 35
TILE_SIZE = 20

OFFSET_X = (WINDOW_X - GRID_X * TILE_SIZE) // 2
OFFSET_Y = (WINDOW_Y - GRID_Y * TILE_SIZE) // 2


def main():

    running = True

    # GRID ERSTELLEN
    GRID = []

    for x in range(GRID_X):
        for y in range(GRID_Y):
            GRID.append((x, y))

    # GAME LOOP
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


if __name__ == "__main__":
    main()
