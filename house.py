from pico2d import *

class House:
    image = None

    def __init__(self):
        self.x = 300.0
        self.y = 400.0
        if self.image == None:
            House.image = load_image('house.png')

    def update(self, frame_time):
        pass

    def draw_bb(self):
        pass
        #draw_rectangle(*self.get_bb())

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        pass
        #return Map.x-1, Map.y-1, Map.x+1, Map.y+1