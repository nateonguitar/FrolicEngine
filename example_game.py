#!/usr/bin/env python

import datetime

from charpy import Game, GameObject, Matrix, MatrixBorder, Vector2
from pynput import keyboard


class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.position = Vector2(x=5, y=0)
        self.matrix = Matrix.empty_sized(rows=3, columns=2, value="0")


class Card(GameObject):
    def __init__(self):
        super().__init__()
        self.position = Vector2(x=2, y=1)
        _matrix = Matrix.empty_sized(rows=6, columns=6, value=" ")
        _matrix[1][1] = "2"
        # ♤ ♡ ♧ ♢
        _matrix[2][1] = "♤"
        border = MatrixBorder()
        self.matrix = _matrix.with_border(border)


class ExampleGame(Game):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.card = Card()
        self.set_on_keydown(self.on_key_down)
        self.show_debug_info = True

    def on_key_down(self, key: keyboard.Key):
        character_key = hasattr(key, "char")
        if character_key:
            if key.char == "a":
                if self.player.position.x > 0:
                    self.player.position.x -= 1
                return
            if key.char == "d":
                if self.player.position.x < 8:
                    self.player.position.x += 1
                return
            if key.char == "w":
                if self.player.position.y > 0:
                    self.player.position.y -= 1
                return
            if key.char == "s":
                if self.player.position.y < 6:
                    self.player.position.y += 1
                return

        # non character keys, like Shift or Ctrl
        else:
            # on escape kill the game
            if key == keyboard.Key.esc:
                # end_game() is from charpy.Game
                self.end_game()
                return

    def update(self, deltatime: datetime.timedelta):
        # deltatime.total_seconds() is a float
        pass

    def draw(self):
        self.screen.draw_matrix(self.card.matrix, self.card.position)
        self.screen.draw_matrix(self.player.matrix, self.player.position)
        super().draw()


# create the game and it should start automatically
game = ExampleGame()
game.start_game()
