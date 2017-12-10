from pico2d import *

from avalanche import Avalanche

class Game_over:
    image = None

    def __init__(self):
        self.x = 400.0
        self.y = 1000.0
        if self.image == None:
            Game_over.image = load_image('resouce\\game_over.png')

    def update(self, frame_time):
        if Avalanche.game_over == 1:
            self.y -= 5
            if self.y <= 300:
                self.y = 300

    def draw(self):
        self.image.draw(self.x, self.y)