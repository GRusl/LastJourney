import pygame


class Button:
    def __init__(self, parent, point, size, size_text=20, text=None, execute=None):
        self.parent = parent

        self.point = point
        self.size = size

        self.size_text = size_text

        self.execute = execute

        self.text = text if text else 'Button {}'.format(id(self))

    def draw(self, text_color=(255, 0, 0), under_gun=0):
        pass

    def get_point(self):
        # print(self.point(*self.parent.screen.get_size()), self.text)
        if type(self.point[0]) == str:
            w, h = self.parent.screen.get_size()
            return tuple(map(lambda x: eval(x.replace('h', str(h)).replace('w', str(w))), self.point))
        else:
            return self.point

    def under_gun(self, pos):
        point = self.get_point()
        return all([point[i] <= pos[i] <= point[i] + self.size[i] for i in range(2)])


class ExampleButton(Button):
    def __init__(self, parent, point, size, size_text=20, text=None, execute=None):
        super().__init__(parent, point, size, size_text, text, execute)

    def draw(self, text_color=(255, 255, 255), under_gun=0):
        colors = (((119, 136, 153), (47, 79, 79)), ((80, 200, 200), (100, 100, 100)),
                  ((100, 100, 100), (50, 50, 50)))[under_gun]

        point = self.get_point()

        text = pygame.font.SysFont('arial', self.size_text).render(self.text, True, text_color)

        pygame.draw.rect(self.parent.screen, colors[0], list(point) + list(self.size))
        pygame.draw.rect(self.parent.screen, colors[1], list(point) + list(self.size), 2)

        h, w = text.get_size()
        x, y = point
        self.parent.screen.blit(text, (x + (self.size[0] - h) // 2, y + (self.size[1] - w) // 2))
