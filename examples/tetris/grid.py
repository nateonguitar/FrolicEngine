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
        super().__init__()
        self.empty_char = '.' # '°'
        self.position = Vector2(x=5, y=0)

        ### Logically build the grid matrix ###
        matrix_size = Vector2(x=13, y=16)

        # fill the matrix with the empty char
        for i in range(0, matrix_size.y):
            row = []
            for j in range(0, matrix_size.x):
                row.append(self.empty_char)
            self.matrix.append(row)
        
        # swap the corners for corner characters
        self.matrix[0][0] = '╔'
        self.matrix[0][matrix_size.x-1] = '╗'
        self.matrix[matrix_size.y-1][0] = '╚'
        self.matrix[matrix_size.y-1][matrix_size.x-1] = '╝'

        # swap top and bottoms with '═' (skipping first and last positions)
        for i in range(1, matrix_size.x-1):
            self.matrix[0][i] = '═'
            self.matrix[matrix_size.y-1][i] = '═'

        # swap left and right sides with '║' (skipping first and last positions)
        for row in self.matrix:
            # we have already swapped the corners, so we can rely on checking that
            if row[0] == self.empty_char:
                row[0] = '║'
                row[matrix_size.x-1] = '║'
