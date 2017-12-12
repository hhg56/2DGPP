import random

from pico2d import *

class Santa:
    image = None

    def __init__(self):
        self.x, self.y = 8000, -800
        if Santa.image == None:
            Santa.image = load_image('resouce\\santa.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)