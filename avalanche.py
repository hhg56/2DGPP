from pico2d import *

from player_and_map import  Player

class Avalanche:
    image = None
    x = 0

    def __init__(self):
        self.x = 350.0
        self.y = 280.0
        self.z = 0
        if self.image == None:
            self.image = load_image('resouce\\avalanche.png')

    def update(self, frame_time):
        if Player.state == 1:
            self.x -= 5

        if self.z > 500:
            self.x+=1
        else:
            self.z+=1

    def draw(self):
        self.image.draw(self.x, self.y)