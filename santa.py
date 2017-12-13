import random

from pico2d import *
from player_and_map import Map

class Santa:
    image = None

    def __init__(self):
        self.x = 7999
        self.y = Map.arr_y[self.x] + 100

        if Santa.image == None:
            Santa.image = load_image('resouce\\santa.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)