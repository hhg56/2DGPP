import random

from pico2d import *

class Map:
    x = None
    y = None
    start_flag = None
    image = None
    arr_x = []
    arr_y = []
    map_move_y_minor = 0

    def __init__(self):
        self.d = 300.0  # graph절편 d값
        self.r = 100.0  # 그래프 반지름 r값
        i = 0
        j = 0
        self.flag = 1
        self.map_move_y_flag = 0

        if Map.start_flag == None:
            for i in range(0, 10):
                self.i = 800*i
                while self.i < 620 + (800*i):
                    Map.arr_x.append(self.i)
                    Map.arr_y.append(self.d - (200*i))
                    self.i += 1

                self.j = 0
                while self.j < 180:
                    Map.arr_x.append(self.j + 620 + (800*i))
                    Map.arr_y.append(self.r * math.cos(self.j / 180.0 * math.pi) + self.d -(200*i) - self.r)
                    self.j += 1

        if Map.image == None:
            Map.image = load_image('ping.png')

    def update(self, frame_time):
        if int(Player.unreal_x) >= (800 * self.flag) - 20 and int(Player.unreal_x) <= (800 * self.flag) + 20:
            self.map_move_y_flag = 1

        if self.map_move_y_flag == 1:
            if Map.map_move_y_minor <= 200 * self.flag:
                Map.map_move_y_minor += 5
                if Map.map_move_y_minor >= 200 * self.flag:
                    self.map_move_y_flag = 0
                    self.flag += 1


    def draw(self):
        for i in range(0, 800*10):
            self.image.draw(Map.arr_x[i] - Player.unreal_x + 380, Map.arr_y[i]*2 - Player.y + Map.map_move_y_minor*2)


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
    jump_before_y = None
    unreal_x = None
    unreal_y = None
    flag = None
    state = None

    def __init__(self):
        Player.x = 300.0
        Player.y = 300.0
        Player.unreal_x = 300.0
        Player.unreal_y = 0
        Player.jump_before_y = 0
        Player.state = self.STOP
        self.jump_flag = 0
        self.frame = random.randint(0, 8)
        self.life_time = 0.0
        self.spin_flag = 0
        self.total_frames = 0.0
        self.dir = 0.0
        self.y_dir = 0.0
        self.jump_dir = 5.0
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
            self.jump_dir -= 0.1
            Player.jump_before_y += self.jump_dir
            if Player.jump_before_y <= (Map.arr_y[int(Player.unreal_x)] + Map.map_move_y_minor):
                self.y_dir = 0
                self.jump_dir = 5.0
                self.jump_flag = 0
                Player.state = self.back_state
            elif self.jump_dir <= 0:
                self.jump_flag = 2
                self.jump_dir = 0
        if self.jump_flag == 2:
            self.jump_dir += 0.2
            Player.jump_before_y -= self.jump_dir
            if Player.jump_before_y <= (Map.arr_y[int(Player.unreal_x)] + Map.map_move_y_minor):
                self.y_dir = 0
                self.jump_dir = 5.0
                self.jump_flag = 0
                Player.state = self.back_state


        Player.unreal_x += (self.dir * distance)
        Player.x += (self.dir * distance)
        if Player.x > 400:
            Player.x = 400

        if self.jump_flag == 1 or self.jump_flag == 2:
            Player.y = Player.jump_before_y
        else:
            Player.y = Map.arr_y[int(Player.unreal_x)] + Map.map_move_y_minor

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
                Player.jump_before_y = Player.y
            elif Player.state in (self.JUMP, ):
                Player.state = self.SPIN
                self.spin_flag = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            if Player.state in (self.SPIN, ):
                self.spin_flag = 0