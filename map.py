import random

from pico2d import *

class Map:

    image = None
    arr_1 = []
    arr_2 = []
    arr_3 = []
    arr_4 = []

    def __init__(self):
        self.i = 0.0
        self.j = 0.0

        self.a = -1
        self.b = 5
        self.c = -1
        self.d = 200

        self.aa = 10
        self.bb = -80
        self.cc = 10
        self.dd = 193

        while self.i < 5.0:
            Map.arr_1.append(self.i*100)
            Map.arr_2.append(self.a * (self.i*self.i*self.i) + self.b * (self.i* self.i) + self.c * self.i + self.d)
            self.i += 0.1

        while self.j < 5.0:
            Map.arr_1.append(self.j*100+500)
            Map.arr_2.append(self.aa * (self.j*self.j*self.j) + self.bb * (self.j* self.j) + self.cc * self.j + self.dd)
            self.j += 0.1

        if Map.image == None:
            Map.image = load_image('ping.png')

    def update(self, frame_time):
        pass

    def draw_bb(self):
        pass
        #draw_rectangle(*self.get_bb())

    def draw(self):
        for i in range(0, 100):
            self.image.draw(Map.arr_1[i], Map.arr_2[i])

    def get_bb(self):
        pass
        #return Map.x-1, Map.y-1, Map.x+1, Map.y+1