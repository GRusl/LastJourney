import os


class Character:
    def __init__(self, name: str, name_color=(255, 255, 255), img_path: str = None):
        self.name = name
        self.name_color = name_color

        self.img_path = img_path

    def info(self):
        return self.name, self.name_color

    def get_img(self, title: str):
        path = f'/img/characters/{self.img_path}/'
        if os.path.exists(path):
            for i in os.listdir(path="."):
                print(i)


class Author(Character):
    def __init__(self):
        super(Author, self).__init__('')
