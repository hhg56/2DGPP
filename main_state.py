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
from game_over import Game_over
from santa import Santa

name = "MainState"

map = None
player = None
house = None
background = None
avalanche = None
coin = None
snows = None
map_on_coins = None
game_over = None
santa = None


def enter():
    game_framework.reset_time()
    global map, player, house, background, avalanche, coin, snows, map_on_coins, game_over, santa
    map = Map()
    player = Player()
    house = House()
    background = Background()
    avalanche = Avalanche()
    coin = Coin()
    game_over = Game_over()
    santa = Santa()
    map_on_coins = [Map_on_Coin() for i in range(200)]
    snows = [Snow() for i in range(20)]
    Player.x = 300.0
    Player.y = 300.0
    Player.unreal_x = 300.0
    Player.unreal_y = 0
    Player.jump_before_y = 0
    Map.map_move_y_minor = 0
    Avalanche.game_over = 0


def exit():
    global map, player, house, background, avalanche, coin, snows, map_on_coins, game_over, santa
    del (map)
    del (player)
    del (house)
    del (background)
    del (avalanche)
    del (coin)
    del (snows)
    del (map_on_coins)
    del (game_over)
    del (santa)


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
    map.update(frame_time)
    house.update(frame_time)
    avalanche.update(frame_time)
    house.update(frame_time)
    coin.update(frame_time)
    game_over.update(frame_time)

    if collide(avalanche, player):
        avalanche.eat(player)
    else:
        player.update(frame_time)

    for map_on_coin in map_on_coins:
        map_on_coin.update(frame_time)

        if collide(map_on_coin, player):
            map_on_coins.remove(map_on_coin)
            player.eat(map_on_coin)

    for snow in snows:
        snow.update(frame_time)

def draw(frame_time):
    clear_canvas()
    background.draw()
    house.draw()
    map.draw()
    for snow in snows:
        snow.draw()
    for map_on_coin in map_on_coins:
        map_on_coin.draw()
    coin.draw()
    player.draw()
    santa.draw()
    avalanche.draw()
    game_over.draw()
    update_canvas()