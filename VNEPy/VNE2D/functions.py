import pygame


def init_windows(self, flags=0):
    pygame.quit()
    pygame.init()

    pygame.mouse.set_visible(False)

    self.screen = pygame.display.set_mode((0, 0) if flags == pygame.FULLSCREEN else (1000, 600), flags=flags)
