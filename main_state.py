import random
import json
import os

from pico2d import *

import game_framework
import title_state


name = "MainState"

boy = None
grass = None
font = None
map = None
boy_flag = 0

arr_1 = []
arr_2 = []

class Map:
    def __init__(self):
        self.image = load_image('ping.png')
        i = 0
        while(i < 100):
            arr_1.append(i)
            arr_2.append(i)
            i += 1

    def draw(self):
        j = 0
        while (j < 100):
            self.image.draw(arr_1[j], arr_2[j])
            j += 1


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        if boy_flag == 0:
            self.frame = (self.frame + 1) % 8
            self.x += self.dir
            if self.x >= 800:
               self.dir = -1
            elif self.x <= 0:
             self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass, map
    boy = Boy()
    grass = Grass()
    map = Map()


def exit():
    global boy, grass, map
    del(boy)
    del(grass)
    del(map)


def pause():
    global boy_flag
    pass


def resume():
    global boy_flag
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            global boy_flag
            if boy_flag == 0:
                boy_flag = 1
            elif boy_flag == 1:
                boy_flag = 0

def update():
    boy.update()


def draw():
    clear_canvas()
    map.draw()
    #grass.draw()
    boy.draw()
    update_canvas()