import sys

from VNEPy.VNE2D.app import App
from VNEPy.VNE2D.functions import *
from VNEPy.VNE2D.interactions import ExampleButton

from plot import fragment

from VNEPy.VNEPy.words import Phrase


class mouse(pygame.sprite.Sprite):  # load and render mouse arrow
    image = pygame.image.load('images/arrow.png')
    image2 = pygame.image.load('images/arrow_1.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = mouse.image2
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - 12
        self.rect.y = pos[1] - 12


class GameApp(App):  # game
    def __init__(self, parent):
        super().__init__(parent)

        self.fragments = [fragment.get()]
        self.i_fragments = 0
        self.i_fragment = 0

        self.text = "342434234"
        self.color_text = (255, 255, 255)

        self.fon_img = pygame.image.load('images/menu_fon.png')

        self.buttons.append(ExampleButton(self.parent, ('5', 'h - 30'), (200, 25), text='Вернуться в главное меню',
                                          execute=lambda: self.parent.set_active_window('menu'), size_text=15))

        self.buttons.append(ExampleButton(self.parent, ('210', 'h - 30'), (200, 25), text='Сохранить',
                                          execute=lambda: print(10), size_text=15))

    def press(self, event):
        if event.pos[1] < self.parent.screen.get_size()[1]:
            if self.i_fragment == len(self.fragments[self.i_fragments]):
                self.i_fragment = 0
                self.i_fragments += 1

            if self.i_fragments == len(self.fragments):
                self.i_fragments = 0
                self.parent.set_active_window('menu')
            else:
                action = self.fragments[self.i_fragments][self.i_fragment]
                if isinstance(action, Phrase):
                    self.text = f'{action.character.name}: {action.text}'
                    self.color_text = action.character.name_color

            self.i_fragment += 1

    def draw(self):
        w, h = self.parent.screen.get_size()

        pygame.draw.rect(self.parent.screen, (0, 0, 0), (0, h - 100, w, h))
        pygame.draw.rect(self.parent.screen, (100, 100, 100), (0, h - 100, w, 10))

        text = pygame.font.SysFont('arial', 20).render(self.text, True, self.color_text)
        w_text, h_text = text.get_size()
        self.parent.screen.blit(text, (20, h - 85 + h_text // 2))


class SettingApp(App):  # screen settings (full_screen, fixed_screen, adjustable_screen)
    def __init__(self, parent):
        super().__init__(parent)

        self.fon_img = pygame.image.load('images/menu_fon.png')

        self.buttons.append(ExampleButton(self.parent, (10, 10), (50, 50),
                                          text='<<<', execute=lambda: self.parent.set_active_window('menu')))
        
        # w, h = self.parent.screen.get_size()
        for n, (i, f) in enumerate((('Полноэкранный', lambda: init_windows(self.parent, pygame.FULLSCREEN)),
                                    ('Фиксированный', lambda: init_windows(self.parent, 0)),
                                    ('Настраиваемый', lambda: init_windows(self.parent, pygame.RESIZABLE)))):
            self.buttons.append(ExampleButton(self.parent, (f'w // 2 - 230 + (155 * {n})', '20'), (150, 40),
                                              text=i, execute=f))


class about_game(App):  # titles about game
    def __init__(self, parent):
        super().__init__(parent)

        self.fon_img = pygame.image.load('images/menu_fon.png')

        self.buttons.append(ExampleButton(self.parent, (10, 10), (50, 50),
                                          text='<<<', execute=lambda: self.parent.set_active_window('menu')))


class MenuApp(App):  # menu
    def __init__(self, parent):
        super().__init__(parent)

        # w, h = self.parent.screen.get_size()

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
        w, h = self.parent.screen.get_size()

        # Load_image.fon(self)
        pygame.draw.aaline(self.parent.screen, (255, 255, 255), [220, 0], [220, w])

        title = pygame.font.SysFont('arial', 50).render('Last Journey', True, (255, 255, 255))
        v = pygame.font.SysFont('arial', 20).render('V0.0.0', True, (255, 255, 255))

        v_w, v_h = v.get_size()
        title_w, title_h = title.get_size()

        self.parent.screen.blit(v, (w - v_w - 20, h - v_h - 20))
        self.parent.screen.blit(title, (w - title_w - 20, h - v_h - title_h - 20))


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

            # print(self.clock.get_fps())

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
