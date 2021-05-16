from game.vector2 import Vector2
from game.matrix import Matrix

class Screen():

    def __init__(self, rows=0, columns=0):
        self._matrix = Matrix.empty_sized(rows=rows, columns=columns, value=None)


    def apply(self, screen):
        """
        Copies the given screen's values over this screen's values.
        Resizes larger as needed.
        """
        if type(screen) is not Screen:
            raise Exception('Tried to apply a non-Screen to a Screen')
        incoming_size = screen.size
        for i in range(0, incoming_size.y):
            for j in range(0, incoming_size.x):
                # will resize the internal matrix if needed inside the set() method
                value = screen.get(y=i, x=j)
                self.set(y=i, x=j, value=value)

    
    def get(self, x, y):
        """
        Gets the value in this screen's matrix at the given x and y indexes.
        Returns None if out of bounds.
        """
        try:
            return self._matrix[y][x]
        except:
            return None


    def set(self, x, y, value):
        """
        Sets the value in this screen's matrix.
        Resizes larger (with None values) if x or y indexes are out of bound.
        """
        current_size = self.size
        diff = Vector2(
            x = x - current_size.x,
            y = y - current_size.y
        )
        if diff.y > 0:
            for i in range(0, diff.y):
                self._matrix.append([])
        if diff.x > 0:
            for row in self._matrix:
                for _x in range(0, diff.x):
                    row.append(None)
        self._matrix[y][x] = value

    @property
    def size(self) -> Vector2:
        return self._matrix.size
