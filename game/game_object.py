from .vector2 import Vector2

class GameObject():

    def __init__(self, **kwargs):
        self.set_matrix(**kwargs)
        self.position = Vector2(x=0, y=0)


    def get_matrix(self) -> list:
        return self.matrix


    def set_matrix(self, rows = 0, columns = 0, matrix = []):
        '''
        Set the size and shape of the matrix.
        Pass rows/columns OR matrix NOT BOTH.
        Must be rectagular. (all rows must be uniform)
        '''
        if type(matrix) is list and len(matrix) == 0 and rows != 0 and columns != 0:
            raise Exception('Game object set_matrix() was called with a starting shape matrix AND rows/columns being set.')

        if rows > 0 or columns > 0:
            self.matrix = [[ 0 for _ in range(columns)] for __ in range(rows)]
        else:
            previous_width = len(matrix[0]) if len(matrix) else 0
            for row in matrix:
                current_width = len(row)
                if current_width != previous_width:
                    raise Exception('Was given a non-rectangular matrix')
                    previous_width = current_width
            self.matrix = matrix


    @property
    def size(self) -> Vector2:
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
