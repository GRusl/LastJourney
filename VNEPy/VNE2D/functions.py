import pygame


def init_windows(self, flags=0):
    pygame.quit()
    pygame.init()

    self.screen = pygame.display.set_mode((1000, 600), flags=flags)

def dip_point(**kwargs):
    def return_f(**kwargs):
        pass
