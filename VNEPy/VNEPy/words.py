class Choice:
    pass


class Fon:
    pass


class Interlocutor:
    pass


class Phrase:
    from . import character

    def __init__(self, text: str, character: character.Character):
        self.text = text
        self.character = character

    def get(self):
        return self.character, self.text


class Fragment:
    def __init__(self, fragment_name: str, fon_img: str = ""):
        self.fragment_name = fragment_name

        self.last_fragment_name = None
        self.actions = []

    def add(self, action):
        self.actions.append(action)

    def end(self, title: str):
        self.last_fragment_name = title

    def get(self):
        return self.actions
