from pico2d import *

class Winter:
    def __init__(self):
        self.image = load_image('winter.png')

    def draw(self):
        self.image.draw(400, 300)