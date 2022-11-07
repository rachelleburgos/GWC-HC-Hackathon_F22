import pygame, sys
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Game") # TODO: Title of the window. Change it later to the title of the game.
        clock = self.clock = pygame.time.Clock()

    def run(self):
        while True: # Main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If the user clicks the exit button,
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000 # Delta time in seconds
            self.display_surface.fill((0, 0, 0)) # Fill the screen with black

            pygame.display.update() # Update the display


if __name__ == '__main__':
    game = Game()
    game.run()