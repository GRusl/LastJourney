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


class mouse(pygame.sprite.Sprite):
    image = pygame.image.load('images/arrow.png')
    image2 = pygame.image.load('images/arrow_1.png')

    def __init__(self, group):
        super().__init__(group)
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        self.image = mouse.image2
        self.rect = self.image.get_rect()
        print(1)

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - 12
        self.rect.y = pos[1] - 12


class GameApp(App):
    def __init__(self, parent):
        super().__init__(parent)

        self.fon_img = pygame.image.load('images/menu_fon.png')

        self.buttons.append(ExampleButton(self.parent, (10, 10), (200, 25), text='Вернуться в главное меню',
                                          execute=lambda: self.parent.set_active_window('menu'), size_text=15))

    def draw(self):
        h, w = self.parent.screen.get_size()

        pygame.draw.rect(self.parent.screen, (0, 0, 0), (0, w - 100, h, w))
        pygame.draw.rect(self.parent.screen, (100, 100, 100), (0, w - 100, h, 10))


class SettingApp(App):
    def __init__(self, parent):
        super().__init__(parent)

        self.fon_img = pygame.image.load('images/menu_fon.png')

        self.buttons.append(ExampleButton(self.parent, (10, 10), (50, 50),
                                          text='<<<', execute=lambda: self.parent.set_active_window('menu')))
        
        # h, w = self.parent.screen.get_size()
        for n, (i, f) in enumerate((('Полноэкранный', lambda: init_windows(self.parent, pygame.FULLSCREEN)),
                                    ('Фиксированный', lambda: init_windows(self.parent, 0)),
                                    ('Настраиваемый', lambda: init_windows(self.parent, pygame.RESIZABLE)))):
            self.buttons.append(ExampleButton(self.parent, (f'h // 2 - 230 + (155 * {n})', '20'), (150, 40),
                                              text=i, execute=f))


class about_game(App):
    def __init__(self, parent):
        super().__init__(parent)

        self.fon_img = pygame.image.load('images/menu_fon.png')

        self.buttons.append(ExampleButton(self.parent, (10, 10), (50, 50),
                                          text='<<<', execute=lambda: self.parent.set_active_window('menu')))


class MenuApp(App):
    def __init__(self, parent):
        super().__init__(parent)

        # h, w = self.parent.screen.get_size()

        self.fon_img = pygame.image.load('images/menu_fon.png')

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

        # Load_image.fon(self)
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

        self.all_sprites = pygame.sprite.Group()
        mouse(self.all_sprites)

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
        self.screen.fill('black')
        pygame.mouse.set_visible(False)

        if 'fon_img' in self.windows[self.active_window].__dict__:
            img_h, img_w = self.windows[self.active_window].fon_img.get_size()
            win_h, win_w = self.screen.get_size()

            difference = min(win_h - img_h, win_w - img_w, key=abs)

            fon = pygame.transform.scale(self.windows[self.active_window].fon_img,
                                         (img_h + difference, img_w + difference))

            self.screen.blit(fon, (-(img_h + difference - win_h) // 2, -(img_w + difference - win_w) // 2))

        self.windows[self.active_window].draws()

        self.all_sprites.draw(self.screen)
        self.all_sprites.update()

        pygame.display.flip()

    def run(self):
        self.run_while = True
        while self.run_while:
            self.draw()  # We are rendering

            print(self.clock.get_fps())

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
