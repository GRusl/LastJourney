class Choice:
    pass


class Fon:
    pass


class Interlocutor:
    pass


class Fragment:
    def __init__(self, fon_img: str):
        self.last_fragment_name = None
        self.actions = []

    def add(self, action):
        self.actions.append(action)

    def end(self, title: str):
        self.last_fragment_name = title

    def get(self):
        for i in self.actions:
            if i:
                yield i
