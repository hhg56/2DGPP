import random
import math

from pico2d import *

class Map:

    image = None
    arr_1 = []
    arr_2 = []

    def __init__(self):
        self.i = 0.0
        self.j = 0.0
        self.d = 300.0
        self.r = 200.0

        while self.i < 620:
            Map.arr_1.append(self.i)
            Map.arr_2.append(self.d)
            self.i += 1

        while self.j < 180:
            Map.arr_1.append(self.j+620)
            Map.arr_2.append(self.r * math.cos(self.j / 180.0 * math.pi) + self.d - self.r)
            self.j += 1

        if Map.image == None:
            Map.image = load_image('ping.png')

    def update(self, frame_time):
        pass

    def draw_bb(self):
        pass
        #draw_rectangle(*self.get_bb())

    def draw(self):
        for i in range(0, 800):
            self.image.draw(Map.arr_1[i], Map.arr_2[i])

    def get_bb(self):
        pass
        #return Map.x-1, Map.y-1, Map.x+1, Map.y+1