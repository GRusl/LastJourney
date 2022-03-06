import os

import pygame


class Character:
    def __init__(self, name: str, name_color=(255, 255, 255), emotion_path: str = "emotion/"):
        self.name = name
        self.name_color = name_color

        START_PATH = f'./images/characters/{name}/'

        # self.emotion_path = emotion_path

        self.emotions = {}
        path = os.path.join(START_PATH, emotion_path)
        if os.path.exists(path):
            for f_name in os.listdir(path=path):
                f_path = os.path.join(path, f_name)
                if os.path.isfile(f_path):
                    self.emotions['.'.join(f_name.split('.')[:-1])] = pygame.image.load(f_path)

        print(self.emotions)

    def info(self):
        return self.name, self.name_color

    '''
    def get_img(self, title: str):
        path = f'/images/characters/{self.img_path}/'
        if os.path.exists(path):
            for i in os.listdir(path="."):
                print(i)
    '''


class Author(Character):
    def __init__(self):
        super(Author, self).__init__('')
