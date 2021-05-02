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
        self.matrix = matrix


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
        _clone = Matrix(rows=_size.y, columns=_size.x)
        for i in range(0, _size.y):
            for j in range(0, _size.x):
                _clone[i][j] = self[i][j]
        return _clone


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
