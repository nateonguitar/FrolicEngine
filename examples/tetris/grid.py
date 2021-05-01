from game.matrix_border import MatrixBorder
from game.vector2 import Vector2
from game.game_object import GameObject

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
        _matrix = []
        
        ### Logically build the grid matrix ###
        matrix_size = Vector2(x=13, y=16)

        # fill the matrix with the empty char
        for i in range(0, matrix_size.y):
            row = []
            for j in range(0, matrix_size.x):
                row.append(self.empty_char)
            _matrix.append(row)

        border = MatrixBorder(sides=MatrixBorder.SINGLE_LINE_THIN)
        _matrix = border.apply_to_matrix(_matrix)
        super().__init__(matrix=_matrix)
