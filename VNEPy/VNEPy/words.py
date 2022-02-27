from ..VNE2D.interactions import Button


class Fon:
    pass


class Interlocutor:
    pass


class Choice:
    def __init__(self, button_type: Button, *buttons_description: tuple[str, str]):
        self.button_type = button_type
        self.buttons_description = buttons_description
        # self.buttons = [button_type() for n, (title, link) in enumerate(buttons_description)]

    def get_buttons(self, big_parent, parent) -> list:
        def set_i_fragments(var):
            def fun():
                parent.i_fragments = var
                parent.i_fragment = 0

            return fun

        return [self.button_type(big_parent, ('w / 2 - 100', f'20 + {n} * 30'), (200, 20), text=text,
                                 execute=set_i_fragments(link))
                for n, (text, link) in enumerate(self.buttons_description)]


class Phrase:
    from . import character

    def __init__(self, text: str, character: character.Character):
        self.text = text
        self.character = character

    def get(self):
        return self.character, self.text


class Fragment:
    def __init__(self, title: str, fon_img: str = ""):
        self.title = title

        self.last_fragment_name = None
        self.actions = []

    def add(self, action):
        self.actions.append(action)

    def end(self, title: str):
        self.last_fragment_name = title

    def get(self):
        return self.actions

    def __len__(self):
        return len(self.actions)


def compile_plot(*fragments: Fragment) -> dict:
    return {fragment.title: fragment for fragment in fragments}
