import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
select_image = None
select_sound = None

start_state, menu_state, exit_state = 1, 2, 3

def enter():
    global image
    global select_image
    global select_state
    global select_sound

    select_state = start_state

    #if image == None:
    image = load_image('resouce\\title.png')
    select_image = load_image('resouce\\title_select.png')
    select_sound = load_wav('resouce\\stomp.wav')
    select_sound.set_volume(32)

def exit():
    global image, select_image, select_state, select_sound
    del(image)
    del(select_image)
    del(select_state)
    del(select_sound)

def handle_events(frame_time):
    global select_state, select_sound
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if select_state == start_state:
                    game_framework.change_state(main_state)
                elif select_state == menu_state:
                    pass
                elif select_state == exit_state:
                    game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                if select_state == start_state:
                    select_state = menu_state
                elif select_state == menu_state:
                    select_state = exit_state
                select_sound.play()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if select_state == menu_state:
                    select_state = start_state
                elif select_state == exit_state:
                    select_state = menu_state
                select_sound.play()

def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)

    if select_state == start_state:
        select_image.draw(220, 235)
    elif select_state == menu_state:
        select_image.draw(220, 160)
    elif select_state == exit_state:
        select_image.draw(220, 75)

    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






