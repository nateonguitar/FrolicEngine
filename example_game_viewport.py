#!/usr/bin/env python

from frolic import Game, GameObject, Matrix, MatrixBorder, Screen, Vector2
from pynput import keyboard


class Tree(GameObject):
    def __init__(self):
        m = Matrix([
            [None, '^',None],
            ['/', '_', '\\'],
            [None, '|',None],
        ])
        super().__init__(matrix=m)



class Background(GameObject):
    def __init__(self):
        m = Matrix.empty_sized(20, 20, '.')
        tree = Tree()
        m = m.apply(tree.matrix, Vector2(2, 2))
        m = m.apply(tree.matrix, Vector2(6, 8))
        m = m.apply(tree.matrix, Vector2(3, 12))
        m = m.apply(tree.matrix, Vector2(12, 15))
        super().__init__(matrix=m)



class Player(GameObject):
    def __init__(self):
        m = Matrix([
            ['o'],
            ['X'],
        ])
        super().__init__(matrix=m)


class Level(GameObject):

    def __init__(self):
        self.background = Background()
        self.player = Player()
        self.player.position = Vector2(2, 2)
        m = Matrix.empty_sized()
        super().__init__(matrix=m)

    def draw(self, screen: Screen):

        display_matrix = self.background.matrix.clone()
        display_matrix = display_matrix.apply(self.player.matrix, self.player.position)
        display_matrix = display_matrix.with_border(MatrixBorder(MatrixBorder.DOUBLE_LINE))

        viewport = Matrix.empty_sized(10, 20)
        player_pos = self.player.position
        offset = viewport.size.scale(0.5)
        offset.x = int(offset.x)
        offset.y = int(offset.y)
        viewport = viewport.apply(display_matrix, Vector2(-player_pos.x + offset.x, -player_pos.y - 1 + offset.y))
        viewport = viewport.with_border(MatrixBorder(MatrixBorder.SINGLE_LINE_THIN))

        screen.draw_matrix(viewport, Vector2(0, 0))


    def on_key_down(self, key: keyboard.Key):
        char = key.char if hasattr(key, "char") else None
        before_player_move_pos = self.player.position.clone()
        if key == keyboard.Key.left or char == "a":
            self.player.position.x -= 1
        if key == keyboard.Key.right or char == "d":
            self.player.position.x += 1
        if key == keyboard.Key.up or char == "w":
            self.player.position.y -= 1
        if key == keyboard.Key.down or char == "s":
            self.player.position.y += 1
        # check if player needs to move back to its previous position from
        # colliding with a wall
        if before_player_move_pos != self.player.position:
            ppos = self.player.position
            bsize = self.background.size
            if ppos.y < 1 or ppos.y >= bsize.y - 2 or ppos.x < 1 or ppos.x >= bsize.x - 1:
                self.player.position = before_player_move_pos



class ExampleViewportGame(Game):
    def __init__(self):
        super().__init__()
        self.level = Level()
        self.set_on_keydown(self.on_key_down)
        self.show_debug_info = True

    def on_key_down(self, key: keyboard.Key):
        self.level.on_key_down(key)
        char = key.char if hasattr(key, "char") else None
        if key == keyboard.Key.esc:
            # end_game() is from frolic.Game
            self.end_game()

    def update(self, deltatime: float):
        # deltatime.total_seconds() is a float
        pass

    def draw(self):
        self.level.draw(self.screen)
        super().draw()


# create the game and it should start automatically
game = ExampleViewportGame()
game.run()
