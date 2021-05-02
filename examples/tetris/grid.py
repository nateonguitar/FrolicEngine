from game.matrix_border import MatrixBorder
from game.vector2 import Vector2
from game.game_object import GameObject
from game.matrix import Matrix

class Grid(GameObject):
    # The matrix will look something like this, but its size
    # is set by the gridsize handed in to the constructor
    # ╔═══╗
    # ║°°°║
    # ║°°°║
    # ║°°°║
    # ╚═══╝

    def __init__(self):
        self.empty_char = '.' # '°'
        self.position = Vector2(x=5, y=0)
        matrix = Matrix.empty_sized(rows=16, columns=13, value='.')
        border = MatrixBorder(sides=MatrixBorder.SINGLE_LINE_THIN)
        matrix = border.apply(matrix)
        super().__init__(matrix=matrix)
