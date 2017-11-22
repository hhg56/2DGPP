import random
import json
import os
import time
import math

from pico2d import *

import game_framework
import title_state

from winter import Winter

name = "MainState"

map = None
player = None
house = None
winter = None
avalanche = None
coin = None

class Coin:
    image = None

    def __init__(self):
        self.x = 650
        self.y = 550
        self.frame = 0
        if self.image == None:
            self.image = load_image('coin.png')

    def update(self, frame_time):
        self.frame += 1
        if self.frame == 6:
            self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 53, 0, 42, 42, self.x, self.y)


class Avalanche:
    image = None
    x = 0

    def __init__(self):
        self.x = 350.0
        self.y = 280.0
        self.z = 0
        if self.image == None:
            self.image = load_image('avalanche.png')

    def update(self, frame_time):
        if Player.state == 1:
            self.x -= 5

        if self.z > 500:
            self.x+=1
        else:
            self.z+=1

    def draw(self):
        self.image.draw(self.x, self.y)


class House:
    image = None

    def __init__(self):
        self.x = 300.0
        self.y = 350.0
        if self.image == None:
            House.image = load_image('house.png')

    def update(self, frame_time):
        if Player.state == 1:
            self.x -= 5

    def draw(self):
        self.image.draw(self.x, self.y)


class Map:
    x = None
    y = None
    start = None
    i = None
    j = None
    image = None
    arr_1 = []
    arr_2 = []
    yy = 0

    def __init__(self):
        self.d = 300.0
        self.r = 100.0
        self.k = 0.0
        i = 0
        j = 0
        self.flag = 1
        self.fflag = 0

        if Map.start == None:
            for i in range(0, 10):
                self.i = 800*i
                while self.i < 620 + (800*i):
                    Map.arr_1.append(self.i)
                    Map.arr_2.append(self.d - (200*i))
                    self.i += 1

                self.j = 0
                while self.j < 180:
                    Map.arr_1.append(self.j + 620 + (800*i))
                    Map.arr_2.append(self.r * math.cos(self.j / 180.0 * math.pi) + self.d -(200*i) - self.r)
                    self.j += 1

        if Map.image == None:
            Map.image = load_image('ping.png')

    def update(self, frame_time):
        if int(Player.xx) >= (800 * self.flag) - 3 and int(Player.xx) <= (800 * self.flag) + 3:
            self.fflag = 1

        if self.fflag == 1:
            if Map.yy <= 200 * self.flag:
                Map.yy += 5
                if Map.yy >= 200 * self.flag:
                    self.fflag = 0
                    self.flag += 1


    def draw(self):
        for i in range(0, 800*10):
            self.image.draw(Map.arr_1[i] - Player.xx + 380, Map.arr_2[i]*2 - Player.y + Map.yy*2)


class Player:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    STAND, RUN, JUMP, STOP, SPIN = 0, 1, 2, 3, 4
    image = None
    x = None
    y = None
    xx = None
    yy = None
    flag = None
    state = None

    def __init__(self):
        Player.x = 300.0
        Player.y = 300.0
        Player.xx = 300.0
        Player.yy = 0
        self.jump_flag = 0
        self.frame = random.randint(0, 8)
        self.life_time = 0.0
        self.spin_flag = 0
        self.total_frames = 0.0
        self.dir = 0.0
        self.y_dir = 0.0
        self.yy_dir = 0.0
        self.back_y = 0
        Player.state = self.STOP
        self.back_state = 0
        if Player.image == None:
            Player.image = load_image('board.png')

    def update(self, frame_time):

        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Player.RUN_SPEED_PPS * frame_time
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time


        if Player.state == self.STAND:
            self.frame = int(self.total_frames) % 2
        elif Player.state == self.RUN:
            self.frame = int(self.total_frames) % 11

            if self.dir >= 1:
                self.dir = 1
            else:
                self.dir += 0.01
        elif Player.state == self.STOP:
            self.frame = int(self.total_frames) % 3

            if self.dir <= 0:
                self.dir = 0
                Player.state = self.STAND
            else:
                self.dir -= 0.05

        if Player.state == self.JUMP:
            self.frame = int(self.total_frames) % 10

        if self.jump_flag == 1:
            self.yy_dir += 0.1
            self.y_dir += self.yy_dir
            if self.yy_dir >= 5:
                self.jump_flag = 2
        if self.jump_flag == 2:
            self.yy_dir -= 0.1
            self.y_dir -= self.yy_dir
            if self.yy_dir <= 0:
                self.y_dir = 0
                self.yy_dir = 0
                Player.y = self.back_y
                self.jump_flag = 0
                Player.state = self.back_state


        Player.xx += (self.dir * distance)
        Player.x += (self.dir * distance)
        if Player.x > 400:
            Player.x = 400

        Player.y = Map.arr_2[int(Player.xx)] + self.y_dir + Map.yy

        Player.x = clamp(0, Player.x, 800)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def draw(self):
        if Player.state == self.STAND:
            self.image.clip_draw(self.frame * 78, 330, 60, 60, self.x, self.y)
        elif Player.state == self.RUN:
            self.image.clip_draw(self.frame * 70, 275, 60, 60, self.x, self.y)
        elif Player.state == self.STOP:
            self.image.clip_draw(0, 140, 44, 60, self.x, self.y)
        elif Player.state == self.JUMP:
            self.image.clip_draw(0, 140, 44, 60, self.x, self.y)
        elif Player.state == self.SPIN:
            self.image.clip_draw(0, 140, 44, 60, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x+20, self.y + 40

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if Player.state in (self.STAND, self.RUN, self.STOP):
                Player.state = self.RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if Player.state in (self.RUN, ):
                Player.state = self.STOP
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if Player.state in (self.RUN, self.STOP):
                if self.dir > 0:
                    Player.state = self.STOP

                if self.dir <= 0:
                    self.dir = 0
                    Player.state = self.STAND
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if Player.state in (self.STAND, ):
                self.back_state = self.STAND
                Player.state = self.JUMP
                self.jump_flag = 1
                self.back_y = Player.y
            elif Player.state in (self.RUN, self.STOP, ):
                self.back_state = self.RUN
                Player.state = self.JUMP
                self.jump_flag = 1
                self.back_y = Player.y
            elif Player.state in (self.JUMP, ):
                Player.state = self.SPIN
                self.spin_flag = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            if Player.state in (self.SPIN, ):
                self.spin_flag = 0

def enter():
    game_framework.reset_time()
    global map, player, house, winter, avalanche, coin
    map = Map()
    player = Player()
    house = House()
    winter = Winter()
    avalanche = Avalanche()
    coin = Coin()


def exit():
    global map, player, house, winter, avalanche, coin
    del (map)
    del (player)
    del (house)
    del (winter)
    del (avalanche)
    del (coin)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        else:
            player.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update(frame_time):
    player.update(frame_time)
    map.update(frame_time)
    house.update(frame_time)
    avalanche.update(frame_time)
    house.update(frame_time)
    coin.update(frame_time)
    delay(0.01)

def draw(frame_time):
    clear_canvas()
    winter.draw()
    house.draw()
    map.draw()
    avalanche.draw()
    coin.draw()
    player.draw()
    update_canvas()