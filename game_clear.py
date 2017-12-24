from pico2d import *

from avalanche import Avalanche
from santa import Santa
from player_and_map import Player

class Game_clear:
    image = None

    def __init__(self):
        self.x = 400.0
        self.y = 1000.0
        if self.image == None:
            Game_clear.image = load_image('resouce\\game_clear.png')
            Game_clear.clear_image = load_image('resouce\\clear_score.png')

            Game_clear.font = load_font('resouce\\ENCR10B.TTF', 60)

    def update(self, frame_time):
        if Santa.game_clear == 1:
            self.y -= 5
            if self.y <= 300:
                self.y = 300

    def draw(self):
        self.image.draw(self.x, self.y)
        self.clear_image.draw(self.x, self.y - 200)
        self.font.draw(630, self.y - 210, '%d' % Player.eat_coin_num,(220,220,0))