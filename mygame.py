import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"


import game_framework
import start_state
import title_state
import control_state
import main_state

from pico2d import *

game_framework.run(start_state)