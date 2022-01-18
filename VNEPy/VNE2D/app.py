import pygame


class App:
    def __init__(self, parent):
        self.parent = parent

        self.buttons = []

    def runs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.parent.run_while = False

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.buttons_press()

        self.run()

    def run(self):
        pass

    def buttons_press(self):
        for n, button in enumerate(self.buttons):
            if button.under_gun(pygame.mouse.get_pos()) and pygame.mouse.get_focused():
                button.execute()

    def draws(self):
        self.draw()
        self.draw_buttons()

    def draw(self):
        pass

    def draw_buttons(self):
        active_element_found = False
        for n, button in enumerate(self.buttons):
            button_status = 0
            if button.under_gun(pygame.mouse.get_pos()) and not active_element_found and pygame.mouse.get_focused():
                button_status = 2 if pygame.mouse.get_pressed(3)[0] else 1
                active_element_found = True

            button.draw(under_gun=button_status)
