# Installation

```
pip install frolic-engine
```

# Creating a basic game

Create a class that inherits from `Game`, provide an `__init__()` and call `super().__init__()`.
Overriding `update()` and `draw()` are required.
```python
import datetime
from frolic import Game

class TestGame(Game):
    def __init__(self):
        super().__init__()

    def update(self, deltatime: datetime.timedelta):
        # deltatime is the time since the previous update call
        # deltatime.total_seconds() is a floating point
        pass

    def draw(self)
        # must call super
        super().draw()
```


Launch the game by calling the game's `run()` function.
This example so far will just produce an empty screen.
```python
from frolic import Game

class TestGame(Game):
    . . .

game = TestGame()
game.run()
```


Handling inputs.
Notice the `keyboard` import.
```python
from frolic import Game
from pynput import keyboard

class TestGame(Game):
    def __init__(self):
        super().__init__()
        self.set_on_keydown(self.on_key_down)

    def on_key_down(self, key: keyboard.Key):
        character_key = hasattr(key, 'char')

        # will show how to use character keys later
        if character_key:
            pass

        # non character keys, like Shift or Ctrl
        else:
            # on escape kill the game
            if key == keyboard.Key.esc:
                # end_game() is inherited from frolic.Game
                self.end_game()
                return
```

To draw characters/symbols to the screen override the `draw()` function.
`self.screen` is a `Screen` object that represents the current frame.
Set values on the screen to have them show up in the console.

```python
from frolic import Game, Matrix, Vector2
class TestGame(Game):
    . . .

    def draw(self):
        # call screen.set() to put a character at a given x, y coordinate
        self.screen.set(x=0, y=0, '#')

        # draw a matrix at a given position by calling screen.draw_matrix()
        position = Vector2(3, 3)
        matrix = Matrix([
            ['#', '#', '#'],
            ['#', '0', '#'],
            ['#', '#', '#'],
        ])
        self.screen.draw_matrix(matrix, position)

        # Matrix also has a convenient way of making a simple matrix by using Matrix.empty_sized():
        #     the following produces:
        #         ['X', 'X']
        #         ['X', 'X']
        #         ['X', 'X']
        matrix2 = Matrix.empty_sized(rows=3, columns=2, value='▢')

        # Note: Matrices are anchored at the top left corner,
        #       so drawing matrix2 at position Vector2(x=1, y=1)
        #       will produce this screen:
        self.screen.draw_matrix(matrix2, Vector2(x=1, y=1))
        # [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # [' ', 'X', 'X', ' ', ' ', ' ', ' ']
        # [' ', 'X', 'X', ' ', ' ', ' ', ' ']
        # [' ', 'X', 'X', ' ', ' ', ' ', ' ']
        # [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # [' ', ' ', ' ', ' ', ' ', ' ', ' ']

        # call super and the Game will handle applying this frame's "screen" to the console window
        super().draw()
```


Instances of `GameObject` are a convenience class to represent objects in the game.
They have a `matrix` that is of type `Matrix` and a `position` that is of type `Vector2`.
```python
from frolic import Game, GameObject, Matrix, Vector2
from pynput import keyboard

class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.position = Vector2(x=5, y=0)
        self.matrix = Matrix.empty_sized(rows=3, columns=2, value='0')
        # self.size is a Vector2 getter representing the size of the current matrix,
        # so in this example self.size.x == 2 because self.matrix has 2 columns
    def moveLeft():
        self.position.x -= 1
    def moveRight():
        self.position.x += 1

class TestGame(Game):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.set_on_keydown(self.on_key_down)

    . . .

    def on_key_down(self, key: keyboard.Key):
        character_key = hasattr(key, 'char')
        if character_key:
            if key.char == 'a':
                if self.player.position.x > 0:
                    self.player.moveLeft()
                return
            if key.char == 'd':
                if self.player.position.x < 10:
                    self.player.moveRight()
                return
        else:
            if key == keyboard.Key.esc:
                self.end_game()
                return

    def draw(self):
        self.screen.draw_matrix(self.player.matrix, self.player.position)
        super().draw()
```


Another convenience is the `MatrixBorder` class, it creates a copy of the given matrix with a border on it.
`MatrixBorder` has a default border of `SINGLE_LINE_THIN` but also has `SINGLE_LINE_THICK` and `DOUBLE_LINE`
```
border = MatrixBorder(sides=MatrixBorder.DOUBLE_LINE)
        °°°°°        ╔═══╗
        °°°°°        ║°°°║
input   °°A°° output ║°A°║
        °°°°°        ║°°°║
        °°°°°        ╚═══╝
```

Borders other than the provided side-characters can also be used:

```
border = MatrixBorder(sides={
    'top': 'X',
    'top_left': 'X',
    'top_right': 'X',
    'left': 'X',
    'right': 'X',
    'bottom': 'X',
    'bottom_left': 'X',
    'bottom_right': 'X',
})
        °°°°°        XXXXX
        °°°°°        X°°°X
input   °°A°° output X°A°X
        °°°°°        X°°°X
        °°°°°        XXXXX
```

```python
class Card(GameObject):
    def __init__(self):
        super().__init__()
        self.position = Vector2(x=2, y=1)
        _matrix = Matrix.empty_sized(rows=6, columns=6, value=' ')
        _matrix[1][1] = '2'
        # ♤ ♡ ♧ ♢
        _matrix[2][1] = '♤'
        border = MatrixBorder() # default to single thin line
        self.matrix = _matrix.with_border(border)
```

# Examples

A simple example to copy/paste

[example_game.py](example_game.py)

Another simple game that creates a viewport (for a game like zelda)

[example_game_viewport.py](example_game_viewport.py)

Tetris

[FrolicEngineTetris](https://github.com/nateonguitar/FrolicEngineTetris)

Bundle-Breaker (a match 3 game)

[FrolicEngineBundleBreaker](https://github.com/nateonguitar/FrolicEngineBundleBreaker)

# Developing Frolic Engine

Clone this project
```
git clone <url for this project>
```

Create a virtual environment [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html) and activate it
```
# windows:
.\venv\Scripts\activate

# linux:
./venv/bin/activate
```


Install this package into venv
```
pip install .
```

Start developing by modifying the `example_game.py` or create some tests.
Remember that this README's examples very closely follow `example_game.py` so changes there should reflect here in this README.
```
python example_game.py
python tests/border.py
python tests/matrix.py
```
