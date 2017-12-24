import random

from pico2d import *
from player_and_map import Player

class Distance:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 50

        if Distance.image == None:
            Distance.image = load_image('resouce\\distance.png')
            Distance.present_image = load_image('resouce\\present.png')

    def update(self, frame_time):
        self.x = 30 + Player.unreal_x / 12

    def draw(self):
        self.image.draw(400, 50)
        self.present_image.draw(self.x, self.y)