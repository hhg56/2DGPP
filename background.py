from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('resouce\\winter.png')

        self.bgm = load_music('resouce\\background.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(400, 300)