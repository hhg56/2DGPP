import sys
import random
import math

from pico2d import *

class Map:
    def __init__(self):
        self.image = load_image('ping.png')

    def draw(self):
