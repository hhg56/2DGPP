from pico2d import *


class Coin:
    image = None

    def __init__(self):
        self.x = 650
        self.y = 550
        self.frame = 0

        if self.image == None:
            self.image = load_image('resouce\\coin.png')

    def update(self, frame_time):
        self.frame += 1
        if self.frame == 6:
            self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 53, 0, 42, 42, self.x, self.y)