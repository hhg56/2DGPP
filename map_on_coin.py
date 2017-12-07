import random

from pico2d import *
from player_and_map import Map
from player_and_map import Player

class Map_on_Coin:
    image = None

    def __init__(self):
        self.x = random.randint(0, 7000)
        self.y = Map.arr_y[self.x]
        self.frame_x = 0
        self.frame_y = 0
        if self.image == None:
            self.image = load_image('resouce\\map_on_coin.png')

    def update(self, frame_time):
        if self.frame_x == 4:
            self.frame_x = 0
            self.frame_y += 1

            if self.frame_y == 4:
                self.frame_y = 0
        else:
            self.frame_x += 1


    def draw(self):
        self.image.clip_draw(self.frame_x * 25, self.frame_y * 26, 25, 26, self.x - Player.unreal_x + 380, self.y*2 - Player.y + Map.map_move_y_minor*2)