import random

from pico2d import *

class Snow:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(5, 790), random.randint(10, 600)
        if Snow.image == None:
            Snow.image = load_image('snow.png')

    def update(self, frame_time):
        self.y -= 1
        if self.y <= 10:
            self.y = 600

    def draw(self):
        self.image.draw(self.x, self.y)