from .matrix import Matrix
from .vector2 import Vector2

class MatrixBorder():
    """
    ```
    MatrixBorder(sides=MatrixBorder.SINGLE_LINE_THIN)
    ```
    """
    SINGLE_LINE_THIN = {
        'top': '─',
        'top_left': '┌',
        'top_right': '┐',
        'left': '│',
        'right': '│',
        'bottom': '─',
        'bottom_left': '└',
        'bottom_right': '┘',
    }
    SINGLE_LINE_THICK = {
        'top': '━',
        'top_left': '┏',
        'top_right': '┓',
        'left': '┃',
        'right': '┃',
        'bottom': '━',
        'bottom_left': '┗',
        'bottom_right': '┛',
    }
    DOUBLE_LINE = {
        'top': '═',
        'top_left': '╔',
        'top_right': '╗',
        'left': '║',
        'right': '║',
        'bottom': '═',
        'bottom_left': '╚',
        'bottom_right': '╝',
    }


    def __init__(self, sides=SINGLE_LINE_THIN):
        self.top          = sides.get('top', None)
        self.top_left     = sides.get('top_left', None)
        self.top_right    = sides.get('top_right', None)
        self.left         = sides.get('left', None)
        self.right        = sides.get('right', None)
        self.bottom       = sides.get('bottom', None)
        self.bottom_left  = sides.get('bottom_left', None)
        self.bottom_right = sides.get('bottom_right', None)
        sides = (
            self.top,
            self.top_left,
            self.top_right,
            self.left,
            self.right,
            self.bottom,
            self.bottom_left,
            self.bottom_right,
        )
        for side in sides:
            if type(side) is not str or len(side) != 1:
                raise Exception('Sides must be a single character each')


    def apply(self, matrix: Matrix) -> Matrix:
        """
        Does not modify the given matrix,
        returns a new Matrix with the outer sides
        replaced with the defined border characters
        ```
              °°°°°        ╔═══╗
              °°°°°        ║°°°║
        input °°A°° output ║°A°║
              °°°°°        ║°°°║
              °°°°°        ╚═══╝
        ```
        """
        size = matrix.size

        # copy the matrix into a new matrix
        # also detect the matrix size for later use
        _matrix = []
        for row in matrix:
            if size.x == 0:
                size.x = len(row)
            _row = []
            for char in row:
                _row.append(char)
            _matrix.append(_row)

        # apply border
        # swap the corners for corner characters
        _matrix[0][0] = self.top_left
        _matrix[0][size.x-1] = self.top_right
        _matrix[size.y-1][0] = self.bottom_left
        _matrix[size.y-1][size.x-1] = self.bottom_right

        # swap top and bottoms with '═' (skipping first and last positions)
        for i in range(1, size.x-1):
            _matrix[0][i] = self.top
            _matrix[size.y-1][i] = self.bottom

        # swap left and right sides with '║' (skipping first and last positions)
        # Note: _matrix[1:-1] is the syntax to get all elements but the first and last
        for row in _matrix[1:-1]:
            row[0] = self.left
            row[size.x-1] = self.right

        return Matrix(_matrix)