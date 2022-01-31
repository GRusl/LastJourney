import sys

from VNEPy.VNE2D.app import App
from VNEPy.VNE2D.functions import *
from VNEPy.VNE2D.interactions import ExampleButton


class Load_image(App):
    def fon(self):
        h, w = self.parent.screen.get_size()
        fon = pygame.transform.scale(pygame.image.load('images/menu_fon.png'), (h, w))
        self.parent.screen.blit(fon, (0, 0))

    def about_game(self):
        h, w = self.parent.screen.get_size()
        image = pygame.transform.scale(pygame.image.load('images/aboutgame.png'), (h, w))
        self.parent.screen.blit(image, (0, 0))


class GameApp(App):
    def __init__(self, parent):
        super().__init__(parent)

        self.buttons.append(ExampleButton(self.parent, (300, 400), (200, 50),
                                          text='<<<', execute=lambda: self.parent.set_active_window('menu')))


class SettingApp(App):
    def __init__(self, parent):
        super().__init__(parent)

        self.buttons.append(ExampleButton(self.parent, (10, 10), (50, 50),
                                          text='<<<', execute=lambda: self.parent.set_active_window('menu')))
        
        # h, w = self.parent.screen.get_size()
        for n, (i, f) in enumerate((('Полноэкранный', lambda: init_windows(self.parent, pygame.FULLSCREEN)),
                                    ('Фиксированный', lambda: init_windows(self.parent, 0)),
                                    ('Настраиваемый', lambda: init_windows(self.parent, pygame.RESIZABLE)))):
            self.buttons.append(ExampleButton(self.parent, (f'h // 2 - 230 + (155 * {n})', '20'), (150, 40),
                                              text=i, execute=f))
    def draw(self):
        Load_image.fon(self)


class about_game(App):
    def __init__(self, parent):
        super().__init__(parent)

        self.buttons.append(ExampleButton(self.parent, (10, 10), (50, 50),
                                          text='<<<', execute=lambda: self.parent.set_active_window('menu')))

    def draw(self):
        Load_image.about_game(self)


class MenuApp(App):
    def __init__(self, parent):
        super().__init__(parent)

        # h, w = self.parent.screen.get_size()

        for n, (i, f) in enumerate((('Новая игра', lambda: self.parent.set_active_window('game')),
                               ('Загрузить', lambda: print(2)),
                               ('Настройки', lambda: self.parent.set_active_window('settings')),
                               ('Об игре', lambda: self.parent.set_active_window('about_game')),
                               ('Выход', lambda: sys.exit()))):
            self.buttons.append(ExampleButton(self.parent, (10, 10 + 55 * n), (200, 50),
                                              text=i, execute=f))

        # init_windows(self.parent, pygame.RESIZABLE)

    def draw(self):
        h, w = self.parent.screen.get_size()

        Load_image.fon(self)
        pygame.draw.aaline(self.parent.screen, (255, 255, 255), [220, 0], [220, w])

        title = pygame.font.SysFont('arial', 50).render('Last Journey', True, (255, 255, 255))
        v = pygame.font.SysFont('arial', 20).render('V0.0.0', True, (255, 255, 255))

        v_h, v_w = v.get_size()
        title_h, title_w = title.get_size()

        self.parent.screen.blit(v, (h - v_h - 20, w - v_w - 20))
        self.parent.screen.blit(title, (h - title_h - 20, w - v_w - title_w - 20))


class VNEApp:
    def __init__(self):
        init_windows(self)

        self.clock = pygame.time.Clock()

        self.run_while = True

        pygame.display.set_caption('Program title')

        self.active_window = 'menu'
        self.windows = {
            'menu': MenuApp(self),
            'game': GameApp(self),
            'settings': SettingApp(self),
            'about_game': about_game(self)
        }

    def set_active_window(self, val):
        self.active_window = val

    def draw(self):
        self.windows[self.active_window].draws()

        pygame.display.flip()

    def run(self):
        self.run_while = True
        while self.run_while:
            self.draw()  # We are rendering

            self.windows[self.active_window].runs()

            '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_while = False
            '''

            self.clock.tick()  # Let's set the frequency of work

        pygame.quit()


if __name__ == '__main__':
    app = VNEApp()
    app.run()
