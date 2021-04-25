import random

from game import Game, Vector2
from pynput import keyboard

from .grid import Grid
from .shape import *

class TetrisGame(Game):

    grid = Grid()
    start_shape_position : Vector2 = None
    shape : Shape = None

    def __init__(self):
        super().__init__()
        self.deltatime = None
        self.start_shape_position = self.grid.position.clone()
        self.start_shape_position.x += int(self.grid.size.x/2) - 2
        self.shape = self.get_next_shape()
        self.set_on_keydown(self.on_key_down)


    def get_next_shape(self):
        shapes = [
            Square,
            Line,
            ForwardsL,
            BackwardsL,
            ForwardsZ,
            BackwardsZ,
            TShape,
        ]
        shape = random.choice(shapes)()
        shape.position = self.start_shape_position.clone()
        return shape


    def on_key_down(self, key):
        if key == keyboard.Key.esc:
            self.end_game()
            return
        
        if key == keyboard.Key.space:
            self.shape = self.get_next_shape()
            return

        key_character = None
        try:
            key_character = key.char
        except:
            pass

        if key_character == 'w':
            self.shape.spin()
            return

        if key_character == 'a':
            self.shape.position.x -= 1
            return

        if key_character == 'd':
            self.shape.position.x += 1
            return


    def update(self, deltatime):
        self.deltatime = deltatime


    def draw(self):
        self.draw_grid()
        self.draw_instructions()
        if self.shape:
            self.draw_shape()
        self.draw_info()
        super().draw()



    def draw_grid(self):
        pos = self.grid.position
        matrix = self.grid.matrix
        for i in range(0, len(matrix)):
            row = matrix[i]
            for j in range(0, len(row)):
                char = row[j]
                x = j + pos.x
                y = i + pos.y
                self.screen[y][x] = char


    def draw_shape(self):
        # Note: Shape positions are NOT relative to the grid position
        matrix = self.shape.matrix
        offset = Vector2(
            x=self.shape.position.x + 1,
            y=self.shape.position.y + 1
        )
        for i in range(0, len(matrix)):
            row = matrix[i]
            for j in range(0, len(row)):
                should_draw = row[j]
                if should_draw:
                    x = j + offset.x
                    y = i + offset.y
                    self.screen[y][x] = self.shape.char


    def draw_instructions(self):
        self.screen[self.grid.position.y + self.grid.size.y][0] = "Press 'w' arrow to spin shape!"


    def draw_info(self):
        left_offset = self.grid.position.x + self.grid.size.x + 2
        info = []
        if self.grid:
            info.append(f'Grid Position:  {self.grid.position}     ')
        if self.shape:
            info.append(f'Shape:          {self.shape}             ')
            info.append(f'Shape Position: {self.shape.position}    ')
        if self.deltatime.microseconds:
            fps = str(int(1000000 / self.deltatime.microseconds))
            info.append(f'FPS:            {fps}                    ')
        for i in range(0, len(info)):
            self.screen[i+1][left_offset] = info[i]
