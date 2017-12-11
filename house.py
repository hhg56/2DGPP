from pico2d import *

from player_and_map import Player

class House:
    image = None

    def __init__(self):
        self.x = 300.0
        self.y = 350.0
        if self.image == None:
            House.image = load_image('resouce\\house.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.draw(self.x - Player.unreal_x + 380, self.y)