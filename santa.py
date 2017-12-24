import random

from pico2d import *
from player_and_map import Map
from player_and_map import Player

class Santa:
    image = None

    def __init__(self):
        self.x = 800*10 + 300
        self.y = Map.arr_y[self.x] + 20

        if Santa.image == None:
            Santa.image = load_image('resouce\\santa.png')

    def update(self, frame_time):
        pass

    def get_bb(self):
        return self.x - Player.unreal_x + 380 - 60, 0, self.x - Player.unreal_x + 380 + 60, 600

    def draw(self):
        self.image.draw(self.x - Player.unreal_x + 380, self.y * 2 - Player.y + Map.map_move_y_minor * 2)