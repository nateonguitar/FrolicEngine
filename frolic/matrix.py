from __future__ import annotations

from frolic.matrix_border import MatrixBorder
from .vector2 import Vector2

class Matrix():
    """
    `Matrix([<matrix_rows>])` is the easy way to set a Matrix
    ```
    Matrix([
        [1,2],
        [3,4],
    ])
    ```
    `Matrix()` will produce an empty matrix
    ```
    []
    ```
    Matrix.empty_sized(rows=2, columns=3) will produce
    ```
    [None, None, None],
    [None, None, None]
    ```
    Matrix.empty_sized(rows=3, columns=1, value='X') will produce
    ```
    ['X'],
    ['X'],
    ['X'],
    ```
    You can set the values in a Matrix with the square [] operators
    ```
    a = Matrix([[1,2,3]])
    a[0][1] = 7
    print(a)
    > will output
    > [1,7,3]
    ```
    """
    def __init__(self, matrix=[]):
        previous_width = len(matrix[0]) if len(matrix) else 0
        for row in matrix:
            current_width = len(row)
            if current_width != previous_width:
                raise Exception('Was given a non-rectangular matrix')
                previous_width = current_width
        self.matrix: list = matrix


    @staticmethod
    def empty_sized(rows=0, columns=0, value=None):
        """
        Basically a named constructor.
        Provide rows and columns and receive a Matrix object.
        """
        matrix = [[ value for _ in range(columns)] for __ in range(rows)]
        return Matrix(matrix=matrix)


    def rotated(self, clockwize=True):
        _size = self.size
        temp_matrix = [ [None for _ in range(_size.y)] for _ in range(_size.x)]
        for row in range(0, _size.y):
            for col in range(0, _size.x):
                if clockwize:
                    temp_matrix[col][(_size.y-1) - row] = self.matrix[row][col]
                else:
                    temp_matrix[(_size.x-1) - col][row] = self.matrix[row][col]
        return Matrix(temp_matrix)


    @property
    def size(self) -> Vector2:
        try:
            x = 0
            y = len(self)
            if y > 0:
                x = len(self[0])
            return Vector2(x=x, y=y)
        except:
            return Vector2.zero()


    def clone(self):
        _size = self.size
        _clone = Matrix.empty_sized(rows=_size.y, columns=_size.x)
        for i in range(0, _size.y):
            for j in range(0, _size.x):
                _clone[i][j] = self[i][j]
        return _clone


    def append(self, to_append):
        if type(to_append) is not list:
            raise Exception('Tried to append a non-list variable to a Matrix')
        self.matrix.append(to_append)


    def with_border(self, border: MatrixBorder):
        """
        Returns a copy of the matrix with the given border applied to it.
        ```
               °°°°°       ╔═══╗
               °°°°°       ║°°°║
        before °°A°° after ║°A°║
               °°°°°       ║°°°║
               °°°°°       ╚═══╝
        ```
        """
        size = self.size
        _matrix = []
        for row in self.matrix:
            if size.x == 0:
                size.x = len(row)
            _row = []
            for char in row:
                _row.append(char)
            _matrix.append(_row)

        # apply border
        # swap the corners for corner characters
        _matrix[0][0] = border.top_left
        _matrix[0][size.x-1] = border.top_right
        _matrix[size.y-1][0] = border.bottom_left
        _matrix[size.y-1][size.x-1] = border.bottom_right

        # swap top and bottoms with '═' (skipping first and last positions)
        for i in range(1, size.x-1):
            _matrix[0][i] = border.top
            _matrix[size.y-1][i] = border.bottom

        # swap left and right sides with '║' (skipping first and last positions)
        # Note: _matrix[1:-1] is the syntax to get all elements but the first and last
        for row in _matrix[1:-1]:
            row[0] = border.left
            row[size.x-1] = border.right

        return Matrix(_matrix)

    
    def section(self, top_left: Vector2, bottom_right: Vector2, allow_overflow: bool=True) -> Matrix:
        """
        Returns a section of the matrix as another matrix.
        `top_left` and `bottom_right` are both inclusive.

        Example:
        ```
        e = Matrix([
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
        ])
        _e = e.section(Vector2(0, 0), Vector2(1, 1))
        # results in
        # Matrix
        # ['a', 'b']
        # ['d', 'e']

        _e = e.section(Vector2(-1, -1), Vector2(1, 1))
        # results in
        # Matrix
        # [None, None, None]
        # [None, a, b]
        # [None, d, e]

        _e = e.section(Vector2(-1, -1), Vector2(1, 1), allow_overflow=False)
        # results in
        # Matrix
        # [a, b]
        # [d, e]

        _e = e.section(Vector2(0, 0), Vector2(0, 0))
        # Matrix
        # [a]
        ```
        """
        m = []
        _size = self.size
        for i in range(top_left.y, bottom_right.y+1):
            row = []
            for j in range(top_left.x, bottom_right.x+1):
                if 0 <= i < _size.y and 0 <= j < _size.x:
                    row.append(self[i][j])
                elif allow_overflow:
                    row.append(None)
            if len(row) > 0:
                m.append(row)

        return Matrix(m)

    
    def apply(self, other: Matrix, position: Vector2, apply_nones: bool = False) -> Matrix:
        """
        Applies other to self in the given location.
        If the position or other's vector size goes out of bounds it gets ignored.
        If `apply_nones` == True it will copy over the None values,
        if left as the default (False) it will skip over applying Nones (Example 2)

        Example:
        ```
        A = Matrix([
            ['.', '.', '.', '.',],
            ['.', '.', '.', '.',],
            ['.', '.', '.', '.',],
            ['.', '.', '.', '.',],
        ])
        X = Matrix([
            ['X', 'X',],
            ['X', 'X',],
        ])
        B = A.apply(X, Vector2(1, 1))
        C = A.apply(X, Vector2(2, 2))
        D = A.apply(X, Vector2(3, 3))
        ```

        Will result in:

        ```
        B [., ., ., .,]
          [., X, X, .,]
          [., X, X, .,]
          [., ., ., .,]

        C [., ., ., .,]
          [., ., ., .,]
          [., ., X, X,]
          [., ., X, X,]

        D [., ., ., .,]
          [., ., ., .,]
          [., ., ., .,]
          [., ., ., X,]
        ```

        ## Apply Nones:
        ```
        `apply_nones=False` (Default)
        A = Matrix([
            ['.', '.', '.', '.',],
            ['.', '.', '.', '.',],
            ['.', '.', '.', '.',],
            ['.', '.', '.', '.',],
        ])
        X = Matrix([
            [None, 'X',  'X',],
            [None, 'X',  'X',],
            [None, None, None],
        ])
        ```

        `apply_nones=True`
        ```
        B = A.apply(X, Vector2(x=0, y=1))
        B [   .,    .,    .,    .,]
          [   .,    X,    X,    .,]
          [   .,    X,    X,    .,]
          [   .,    .,    .,    .,]

        B = A.apply(X, Vector2(x=0, y=1), apply_nones=True)
        B [   .,    .     .,    .,]
          [None,    X,    X,    .,]
          [None,    X,    X,    .,]
          [None, None, None,    .,]
        ```
        """
        m = self.clone()
        self_size = self.size
        other_size = other.size
        for i in range(other_size.y):
            for j in range(other_size.x):
                charpos = Vector2(x=j+position.x, y=i+position.y)
                if 0 <= charpos.y < self_size.y and 0 <= charpos.x < self_size.x:
                    char = other.matrix[i][j]
                    if char is not None or (char is None and apply_nones):
                        m[charpos.y][charpos.x] = char
        return m


    def __str__(self):
        if (len(self.matrix)) == 0:
            return '[]'
        value = 'Matrix\n'
        for row in self.matrix:
            _row = [str(item) for item in row]
            value += '[' + ', '.join(_row) + "]\n"
        return value


    def __getitem__(self, index):
        return self.matrix[index]

    
    def __setitem__(self, index, data):
        self.matrix[index] = data


    def __len__(self):
        return len(self.matrix)
