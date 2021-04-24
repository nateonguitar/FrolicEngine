from game import Game, Position
from pynput import keyboard
from .shape import *

class TetrisGame(Game):

    shape_instance = None
    grid_position = Position(x=1, y=1)

    def __init__(self):
        super().__init__()
        self.shape_instance = self.get_next_shape()
        self.start_shape_position = Position(x=0, y=0)
        self.shape_instance.position = self.start_shape_position.clone()
        self.set_on_keydown(self.on_key_down)
        self.ready = True


    def get_next_shape(self):
        # TODO: randomize this
        return Line()


    def on_key_down(self, key):
        if key == keyboard.Key.esc:
            self.end_game()
            return

        key_character = None
        try:
            key_character = key.char
        except:
            pass

        if key_character == 'w':
            self.shape_instance.spin()

        if key_character == 'a':
            self.shape_instance.position.x -= 1

        if key_character == 'd':
            self.shape_instance.position.x += 1


    def update(self):
        pass


    def draw(self):
        self.draw_instructions()
        self.draw_grid()
        if self.shape_instance:
            self.draw_shape()
        super().draw()


    def draw_instructions(self):
        self.screen[0][0] = "Press 'w' arrow to spin shape!"

    def draw_grid(self):
        # left row row doesnt show, keep spaces
        matrix = [
            [ '╔', '═', '═', '═', '═', '═', '═', '╗'],
            [ '║', '°', '°', '°', '°', '°', '°', '║'],
            [ '║', '°', '°', '°', '°', '°', '°', '║'],
            [ '║', '°', '°', '°', '°', '°', '°', '║'],
            [ '║', '°', '°', '°', '°', '°', '°', '║'],
            [ '║', '°', '°', '°', '°', '°', '°', '║'],
            [ '║', '°', '°', '°', '°', '°', '°', '║'],
            [ '║', '°', '°', '°', '°', '°', '°', '║'],
            [ '╚', '═', '═', '═', '═', '═', '═', '╝'],
        ]
        for i in range(0, len(matrix)):
            row = matrix[i]
            for j in range(0, len(row)):
                char = row[j]
                x = j + self.grid_position.x
                y = i + self.grid_position.y
                self.screen[y][x] = char


    def draw_shape(self):
        matrix = self.shape_instance.matrix
        for i in range(0, len(matrix)):
            row = matrix[i]
            for j in range(0, len(row)):
                should_draw = row[j]
                
                if should_draw:
                    x = j + self.shape_instance.position.x + self.grid_position.x + 1
                    y = i + self.shape_instance.position.y + self.grid_position.y + 1
                    self.screen[y][x] = self.shape_instance.char
