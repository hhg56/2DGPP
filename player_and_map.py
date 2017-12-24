import random

from pico2d import *

class Map:
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

        if Map.image == None:
            self.i = 0
            for i in range(0, 11):
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

            Map.image = load_image('resouce\\ping.png')

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
        for i in range(0, 800*11):
            self.image.draw(Map.arr_x[i] - Player.unreal_x + 380, Map.arr_y[i]*2 - Player.y + Map.map_move_y_minor*2)
            i += 5


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
    fast_image = None
    more_fast_image = None
    most_fast_image = None
    eat_sound = None
    jump_sound = None
    spin_sound = None
    font = None

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
        self.spin_energy = 0
        self.spin_fast = 0
        self.total_frames = 0.0
        self.dir = 0.0
        self.y_dir = 0.0
        self.jump_dir = 5.0
        self.back_state = 0
        self.eat_coin_num = 0
        if Player.image == None:
            Player.image = load_image('resouce\\board.png')
            Player.fast_image = load_image('resouce\\spin_speed_fast.png')
            Player.more_fast_image = load_image('resouce\\spin_speed_more_fast.png')
            Player.most_fast_image = load_image('resouce\\spin_speed_most_fast.png')

            Player.font = load_font('resouce\\ENCR10B.TTF', 35)

            Player.spin_sound = load_wav('resouce\\spin.wav')
            Player.spin_sound.set_volume(32)
            Player.jump_sound = load_wav('resouce\\jump.wav')
            Player.jump_sound.set_volume(32)
            Player.eat_sound = load_wav('resouce\\coin.wav')
            Player.eat_sound.set_volume(32)

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
            if self.spin_fast == 0:
                if self.dir >= 1:
                    self.dir = 1
                else:
                    self.dir +=0.01
            elif self.spin_fast == 1:
                if self.dir >= 1.1:
                    self.dir = 1.1
                else:
                    self.dir +=0.01
            elif self.spin_fast == 2:
                if self.dir >= 1.2:
                    self.dir = 1.2
                else:
                    self.dir +=0.01
            elif self.spin_fast >= 3:
                if self.dir >= 1.3:
                    self.dir = 1.3
                else:
                    self.dir +=0.01
            else:
                self.dir += 0.01
        elif Player.state == self.STOP:
            self.frame = int(self.total_frames) % 3
            if self.dir <= 0:
                self.dir = 0
                Player.state = self.STAND
            else:
                self.dir -= 0.05
        elif Player.state == self.JUMP:
            self.frame = int(self.total_frames) % 10
        elif Player.state == self.SPIN:
            self.frame = int(self.total_frames) % 4
            self.spin_energy += 5
            if self.spin_energy == 100:
                self.spin_energy = 0

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

        if self.spin_flag == 1:
            if self.spin_fast >= 3:
                self.spin_fast = 3
                self.spin_energy = 100
            else:
                self.spin_energy += 1
                if self.spin_energy >= 100:
                    self.spin_energy = 0
                    self.spin_fast += 1

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
            self.image.clip_draw(self.frame * 60, 70, 60, 70, self.x, self.y)
            if self.spin_fast == 0:
                self.fast_image.clip_draw(0, 0, self.spin_energy, 10, self.x - 50 + self.spin_energy/2, self.y + 40)
            elif self.spin_fast == 1:
                self.more_fast_image.clip_draw(0, 0, self.spin_energy, 10, self.x - 50 + self.spin_energy/2, self.y + 40)
            elif self.spin_fast == 2 or self.spin_fast == 3:
                self.most_fast_image.clip_draw(0, 0, self.spin_energy, 10, self.x - 50 + self.spin_energy/2, self.y + 40)

        Player.font.draw(680, 550, '%d' % self.eat_coin_num,(255,255,0))

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x+20, self.y + 30

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
                Player.jump_before_y = Player.y
                self.jump_sound.play()
            elif Player.state in (self.STOP, ):
                self.back_state = self.STOP
                Player.state = self.JUMP
                self.jump_flag = 1
                Player.jump_before_y = Player.y
                self.jump_sound.play()
            elif Player.state in (self.RUN, ):
                self.back_state = self.RUN
                Player.state = self.JUMP
                self.jump_flag = 1
                Player.jump_before_y = Player.y
                self.jump_sound.play()
            elif Player.state in (self.JUMP, ):
                Player.state = self.SPIN
                self.spin_flag = 1
                self.spin_fast = 0
                self.spin_energy = 0
                self.spin_sound.play()
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            if Player.state in (self.SPIN, ):
                Player.state = self.JUMP
                self.spin_flag = 0

    def eat(self, map_on_coin):
        self.eat_sound.play()
        self.eat_coin_num += 1