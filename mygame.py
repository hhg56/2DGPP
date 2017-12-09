import game_framework
import start_state
import title_state
import main_state

from pico2d import *

open_canvas()
game_framework.run(main_state)
close_canvas()