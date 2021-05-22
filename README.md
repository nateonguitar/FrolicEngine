# Python Text Game Engine

### Install

```
pip install charpy
```

## Example

To see a full Tetris example see
`https://github.com/nateonguitar/CharPyTetris`

Copy/paste this to do a simple test

```python
import charpy
from pynput import keyboard

class Player(charpy.GameObject):
    def __init__(self):
        self.position = charpy.Vector2(x=5, y=0)
        matrix = charpy.Matrix.empty_sized(rows=3, columns=2, value='0')
        super().__init__(matrix=matrix)

class TestGame(charpy.Game):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.set_on_keydown(self.on_key_down)
        self.game_loop()

    def on_key_down(self, key: keyboard.Key):
        # on escape kill the game
        if key == keyboard.Key.esc:
            # end_game() is from charpy.Game
            self.end_game()
            return
        key_character = None
        try:
            key_character = key.char
        except:
            pass
        if key_character == 'a':
            if self.player.position.x > 0:
                self.player.position.x -= 1
            return
        if key_character == 'd':
            if self.player.position.x < 10:
                self.player.position.x += 1
            return
        if key_character == 'w':
            if self.player.position.y > 0:
                self.player.position.y -= 1
            return
        if key_character == 's':
            if self.player.position.y < 5:
                self.player.position.y += 1
            return

    def update(self, deltatime: float):
        pass

    def draw(self):
        self.screen.draw_matrix(self.player.matrix, self.player.position)
        super().draw()

# create the game and it should start automatically
game = TestGame()
```
