from frolic.vector2 import Vector2
from frolic.matrix import Matrix

class Screen():

    def __init__(self, rows=0, columns=0):
        # _matrix is intended to only be modified
        # by this or other instances of the Screen class
        self._matrix = Matrix.empty_sized(rows=rows, columns=columns, value=None)


    def draw_matrix(self, matrix: Matrix, position: Vector2):
        if type(matrix) is not Matrix:
            raise Exception('screen.draw_matrix(matrix, position) matrix must be of type Matrix')
        if type(position) is not Vector2:
            raise Exception('screen.draw_matrix(matrix, position) position must be of type Vector2')
        for i in range(0, len(matrix)):
            row = matrix[i]
            for j in range(0, len(row)):
                char = row[j]
                if char == None:
                    continue
                x = j + int(position.x)
                y = i + int(position.y)
                self.set(y=y, x=x, char=char)


    def draw_string(self, string: str, position: Vector2):
        self.draw_matrix(Matrix([string]), position)


    def apply(self, screen):
        if type(screen) is not Screen:
            raise Exception('the provided screen was not of type Screen')
        self._matrix = screen._matrix

    
    def get(self, x, y):
        """
        Gets the value in this screen's matrix at the given x and y indexes.
        Returns None if out of bounds.
        """
        try:
            return self._matrix[y][x]
        except:
            return None


    def set(self, x, y, char):
        """
        Sets the char in this screen's matrix.
        Resizes larger (with None values) if x or y indexes are out of bound.
        """
        current_size = self.size
        diff = Vector2(
            x = x + 1 - current_size.x,
            y = y + 1 - current_size.y
        )
        if diff.y > 0:
            for i in range(0, diff.y+1):
                expanded_row = [None for j in range(0, current_size.x)]
                self._matrix.append(expanded_row)
        if diff.x > 0:
            for row in self._matrix:
                for _x in range(0, diff.x+1):
                    row.append(None)
        self._matrix[y][x] = char

    @property
    def size(self) -> Vector2:
        return self._matrix.size
