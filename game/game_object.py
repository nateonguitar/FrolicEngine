from .vector2 import Vector2

class GameObject():

    def __init__(self):
        self.matrix = []
        self.position = Vector2(x=0, y=0)

    @property
    def size(self):
        try:
            x = 0
            y = len(self.matrix)
            # detect the longest list inside of the matrix.
            # nothing is keeping our matrix from being non-uniform.
            for i in range(0, len(self.matrix)):
                if len(self.matrix[i]) > x:
                    x = len(self.matrix[i])
            return Vector2(x=x, y=y)
        except:
            return Vector2.zero()

    # currently only works with a rectangular matrix
    def spinClockwise(self):
        num_rows = len(self.matrix) 
        num_cols = len(self.matrix[0])
        temp_matrix  = [[ 0 for _ in range(num_rows)] for _ in range(num_cols)]
        for row in range(0, num_rows):
            for col in range(0, num_cols):
                temp_matrix[col][num_rows - row - 1] = self.matrix[row][col]
        self.matrix = temp_matrix

    def spinCounterClockwise(self):
        num_rows = len(self.matrix) 
        num_cols = len(self.matrix[0])
        temp_matrix  = [[ 0 for _ in range(num_rows)] for _ in range(num_cols)]
        for row in range(0, num_rows):
            for col in range(0, num_cols):
                temp_matrix[num_cols - 1 - col][row] = self.matrix[row][col]

        self.matrix = temp_matrix