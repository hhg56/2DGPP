from pico2d import *

from player_and_map import Player

class Avalanche:
    image = None
    game_over = None

    def __init__(self):
        self.x = -400.0
        self.y = 280.0
        self.speed_up = 0.0
        self.speed_up_count = 0
        self.z = 0
        self.eat_palyer = 0
        if self.image == None:
            self.image = load_image('resouce\\avalanche.png')

    def update(self, frame_time):
        if self.eat_palyer == 1:
            if self.speed_up_count <= 300:
                self.speed_up = 1
                self.x += self.speed_up
                self.speed_up_count += 1
            else:
                self.speed_up = 0
                
        else:
            if self.z > 10:
                self.speed_up+=0.01
                self.x += self.speed_up
            else:
                self.z+=1

    def draw(self):
        self.image.draw(self.x - Player.unreal_x + 380, self.y)

    def get_bb(self):
        return self.x - Player.unreal_x + 380 - 600, self.y - 300 ,self.x - Player.unreal_x + 380 + 400, self.y + 300

    def eat(self, player):
        self.eat_palyer = 1
        Avalanche.game_over = 1