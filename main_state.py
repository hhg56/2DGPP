import random
import json
import os
import time

from pico2d import *

import game_framework
import title_state

from map import Map
from player import Player
from house import House

name = "MainState"

map = None
player = None
house = None

def enter():
    game_framework.reset_time()
    global map, player, house
    map = Map()
    player = Player()
    house = House()


def exit():
    global map, player, house
    del (map)
    del (player)
    del (house)


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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            Player.flag = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_d):
            Player.flag = 0


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
    delay(0.01)

def draw(frame_time):
    clear_canvas()
    house.draw()
    map.draw()
    player.draw()
    update_canvas()