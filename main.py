import sys

from VNEPy.VNE2D.app import App  # Импорт приложения
from VNEPy.VNE2D.functions import *  # Импорт вспомогательных функций
from VNEPy.VNE2D.interactions import ExampleButton  # Импорт кнопки

from plot import plot  # Импорт сюжета

from VNEPy.VNEPy.words import Phrase, Choice, Fon  # Импорт инструментов составления сюжета


class Mouse(pygame.sprite.Sprite):  # Класс кастомизированной мышки
    image = pygame.image.load('images/arrow.png')
    image2 = pygame.image.load('images/arrow_1.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Mouse.image2
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - 12
        self.rect.y = pos[1] - 12


class GameApp(App):  # Приложение игры
    def __init__(self, parent):
        super().__init__(parent)

        # Сюжет
        self.plot = plot
        self.i_fragments = '123'
        self.i_fragment = 0

        # Данные вывода
        self.text = "Нажимая на активную область экрана, вы соглашаетесь с всем, что идет дальше)"
        self.color_text = (255, 255, 255)

        self.choice_buttons = []

        self.fon_img = pygame.image.load('images/menu_fon.png')

        # Статичные кнопки приложения
        self.buttons.append(ExampleButton(self.parent, ('5', 'h - 30'), (200, 25), text='Вернуться в главное меню',
                                          execute=lambda: self.parent.set_active_window('menu'), size_text=15))

        self.buttons.append(ExampleButton(self.parent, ('210', 'h - 30'), (200, 25), text='Сохранить',
                                          execute=lambda: print(10), size_text=15))

    def press(self, event=None):  # Событие нажатия мыши
        if not event or event.pos[1] < self.parent.screen.get_size()[1]:
            next_step = False
            print(self.plot, self.i_fragments, self.i_fragment)
            if self.i_fragment < len(self.plot[self.i_fragments]):
                action = self.plot[self.i_fragments].get()[self.i_fragment]
                if isinstance(action, Phrase):  # Дейстивие является фразой
                    self.text = f'{action.character.name}: {action.text}'
                    self.color_text = action.character.name_color

                    if self.choice_buttons:
                        for i in self.choice_buttons:
                            del self.buttons[(self.buttons.index(i))]

                        self.choice_buttons = []
                elif isinstance(action, Choice):  # Дейстивие является выбором
                    self.choice_buttons = action.get_buttons(self.parent, self)
                    self.buttons += self.choice_buttons
                elif isinstance(action, Fon):  # Изменение фона
                    self.fon_img = pygame.image.load(action.path)
                    next_step = True

                self.i_fragment += 1

                if next_step:
                    self.press()

    def draw(self):  # Отрисовка
        w, h = self.parent.screen.get_size()

        # Интерфейс
        pygame.draw.rect(self.parent.screen, (0, 0, 0), (0, h - 100, w, h))
        pygame.draw.rect(self.parent.screen, (100, 100, 100), (0, h - 100, w, 10))

        # Игровые даннные
        text = pygame.font.SysFont('arial', 20).render(self.text, True, self.color_text)
        w_text, h_text = text.get_size()
        self.parent.screen.blit(text, (20, h - 85 + h_text // 2))


class SettingApp(App):  # screen settings (full_screen, fixed_screen, adjustable_screen)
    def __init__(self, parent):
        super().__init__(parent)

        self.fon_img = pygame.image.load('images/menu_fon.png')

        # Кнопка выхода
        self.buttons.append(ExampleButton(self.parent, (10, 10), (50, 50),
                                          text='<<<', execute=lambda: self.parent.set_active_window('menu')))
        
        # Кнопки настройки режима окна
        for n, (i, f) in enumerate((('Полноэкранный', lambda: init_windows(self.parent, pygame.FULLSCREEN)),
                                    ('Фиксированный', lambda: init_windows(self.parent, 0)),
                                    ('Настраиваемый', lambda: init_windows(self.parent, pygame.RESIZABLE)))):
            self.buttons.append(ExampleButton(self.parent, (f'w // 2 - 230 + (155 * {n})', '20'), (150, 40),
                                              text=i, execute=f))


class about_game(App):  # Об игре
    def __init__(self, parent):
        super().__init__(parent)

        self.fon_img = pygame.image.load('images/menu_fon.png')  # Фон

        # Кнопка выхода
        self.buttons.append(ExampleButton(self.parent, (10, 10), (50, 50),
                                          text='<<<', execute=lambda: self.parent.set_active_window('menu')))

    def draw(self):
        texts = """Постапокалипсис. 
        Две девочки, Тито и Юри, остаются наедине с мёртвой цивилизацией.
        Они путешествуют по руинам безжизненных городов в поисках еды и топлива. 
        Серые и безнадёжные дни сменяют друг друга, но, пока девочки вместе, 
        даже в самых мрачных моментах они находят что-то светлое.
        Что же такое "обычная жизнь" для девочек, блуждающих среди руин?""".splitlines()

        y = 60
        for text_str in texts:
            text = pygame.font.SysFont('arial', 25).render(text_str.strip(), True, (255, 255, 255))
            w, h = text.get_size()

            self.parent.screen.blit(text, (30, y))
            y += h


class MenuApp(App):  # Главное меню
    def __init__(self, parent):
        super().__init__(parent)

        # w, h = self.parent.screen.get_size()

        self.fon_img = pygame.image.load('images/menu_fon.png')  # Фон

        # Кнопки интерфейса
        for n, (i, f) in enumerate((('Новая игра', lambda: self.parent.set_active_window('game')),
                               ('Загрузить', lambda: print(2)),
                               ('Настройки', lambda: self.parent.set_active_window('settings')),
                               ('Об игре', lambda: self.parent.set_active_window('about_game')),
                               ('Выход', lambda: sys.exit()))):
            self.buttons.append(ExampleButton(self.parent, (10, 10 + 55 * n), (200, 50),
                                              text=i, execute=f))

        # init_windows(self.parent, pygame.RESIZABLE)

    def draw(self):  # Отрисовка
        w, h = self.parent.screen.get_size()

        # Load_image.fon(self)
        pygame.draw.aaline(self.parent.screen, (255, 255, 255), [220, 0], [220, w])  # Рахделительная линияв

        # Название и версия
        title = pygame.font.SysFont('arial', 50).render('Last Journey', True, (255, 255, 255))
        v = pygame.font.SysFont('arial', 20).render('V0.0.0', True, (255, 255, 255))

        v_w, v_h = v.get_size()
        title_w, title_h = title.get_size()

        self.parent.screen.blit(v, (w - v_w - 20, h - v_h - 20))
        self.parent.screen.blit(title, (w - title_w - 20, h - v_h - title_h - 20))


class VNEApp:  # Главное приложение
    def __init__(self):
        init_windows(self)

        self.clock = pygame.time.Clock()  # Управление частотой

        self.run_while = True  # Приложение будет цыклично обновляться

        # Кастомизация мыши
        self.all_sprites = pygame.sprite.Group()
        Mouse(self.all_sprites)
        pygame.mouse.set_visible(False)

        self.active_window = 'menu'  # Активное приложение
        self.windows = {  # Список приложений
            'menu': MenuApp(self),
            'game': GameApp(self),
            'settings': SettingApp(self),
            'about_game': about_game(self)
        }

    def set_active_window(self, val):  # Функция обновления активного приложения
        self.active_window = val

    def draw(self):
        self.screen.fill('black')

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

            pygame.display.set_caption(str(self.clock.get_fps()))

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
