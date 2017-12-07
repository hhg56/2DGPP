import random
import json
import os
import time
import math

from pico2d import *

import game_framework
import title_state

from background import Background
from player_and_map import Player
from player_and_map import Map
from coin import Coin
from map_on_coin import Map_on_Coin
from avalanche import Avalanche
from house import House
from snow import Snow

name = "MainState"

map = None
player = None
house = None
background = None
avalanche = None
coin = None
snows = None
map_on_coins = None


def enter():
    game_framework.reset_time()
    global map, player, house, background, avalanche, coin, snows, map_on_coins
    map = Map()
    player = Player()
    house = House()
    background = Background()
    avalanche = Avalanche()
    coin = Coin()
    map_on_coins = [Map_on_Coin() for i in range(200)]
    snows = [Snow() for i in range(20)]


def exit():
    global map, player, house, background, avalanche, coin, snows, map_on_coins
    del (map)
    del (player)
    del (house)
    del (background)
    del (avalanche)
    del (coin)
    del (snows)
    del (map_on_coins)


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
    for map_on_coin in map_on_coins:
        map_on_coin.update(frame_time)
    for snow in snows:
        snow.update(frame_time)
    delay(0.01)

def draw(frame_time):
    clear_canvas()
    background.draw()
    house.draw()
    map.draw()
    avalanche.draw()
    for snow in snows:
        snow.draw()
    for map_on_coin in map_on_coins:
        map_on_coin.draw()
    coin.draw()
    player.draw()
    update_canvas()