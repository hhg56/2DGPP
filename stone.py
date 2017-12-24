import random

from pico2d import *
from player_and_map import Map
from player_and_map import Player

class Stone:
    image = None

    def __init__(self):
        self.x = random.randint(0, 8000)
        self.y = Map.arr_y[self.x]

        if Stone.image == None:
            Stone.image = load_image('resouce\\stone.png')

    def update(self, frame_time):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
         return self.x - Player.unreal_x + 380 - 21, self.y*2 - Player.y + Map.map_move_y_minor*2 - 16, self.x - Player.unreal_x + 380 + 21, self.y*2 - Player.y + Map.map_move_y_minor*2 + 16

    def draw(self):
        self.image.draw(self.x - Player.unreal_x + 380, self.y*2 - Player.y + Map.map_move_y_minor*2)