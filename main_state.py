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
cha_d = 0
cha_x = 0
cha_y = 0

arr_1 = []
arr_2 = []
arr_3 = []
arr_4 = []

class Map:
    def __init__(self):
        self.image = load_image('ping.png')

    def update(self):
        global cha_x
        global cha_y
        arr_1.clear()
        arr_2.clear()
        arr_3.clear()
        arr_4.clear()
        i = 0
        while(i < 10.0):
            x = 10*i - cha_x
            y = 100 * math.cos(i/math.pi) + 600 - cha_y
            arr_1.append(x)
            arr_2.append(y)
            i += 0.1

        j = 0
        while(j < 50.0):
            x = 20 * j + 100 - cha_x
            y =  -j + 500 - cha_y
            arr_3.append(x)
            arr_4.append(y)
            j += 0.1

    def draw(self):
        j = 0
        while (j < 100):
            self.image.draw(arr_1[j], arr_2[j])
            j += 1

        j = 0
        while (j < 100):
            self.image.draw(arr_3[j], arr_4[j])
            j += 1

        j = 0
        while (j < 100):
            self.image.draw(arr_1[j]+300, arr_2[j]-200 - 10)
            j += 1

        j = 0
        while (j < 100):
            self.image.draw(arr_3[j]+300, arr_4[j]-200- 10)
            j += 1

        j = 0
        while (j < 100):
            self.image.draw(arr_1[j] + 600, arr_2[j] - 400 - 20)
            j += 1


class Charicter:
    global cha_x
    global cha_y

    def __init__(self):
        self.x = 100
        self.y = 250
        self.dir = 0.0

    def update(self):
        global cha_x
        global cha_y

        if cha_d == 0:
            self.dir = 0
        elif cha_d == 1:
            self.dir += 0.1
        elif cha_d == 2:
            self.dir -= 0.1
            if self.dir <= 0:
                self.dir = 0
                self.cha_d = 0

        if cha_x > 100:
            if cha_x < 200:

                self.y -= self.dir

        self.x += self.dir
        cha_x = self.x
        cha_y = self.y

    def draw(self):
        draw_rectangle(cha_x, cha_y, cha_x+20, cha_y+50)

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
    global boy, grass, map, charicter
    boy = Boy()
    grass = Grass()
    map = Map()
    charicter = Charicter()


def exit():
    global boy, grass, map, charicter
    del(boy)
    del(grass)
    del(map)
    del(charicter)


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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
            global cha_d
            if cha_d == 0:
                cha_d = 1
            elif cha_d == 1:
                cha_d = 1
            elif cha_d == 2:
                cha_d = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_d:
            if cha_d == 1:
                cha_d = 2


def update():
    boy.update()
    charicter.update()
    map.update()


def draw():
    clear_canvas()
    map.draw()
    charicter.draw()
    boy.draw()
    update_canvas()
    delay(0.01)