from .vector2 import Vector2
from charpy.matrix import Matrix

class GameObject():

    def __init__(self, **kwargs):
        # for type hinting
        self._matrix: Matrix = None
        # set the real thing
        self.matrix = kwargs.get('matrix', Matrix())

        self.position = Vector2(x=0, y=0)


    @property
    def matrix(self):
        return self._matrix


    @matrix.setter
    def matrix(self, value):
        if type(value) is not Matrix:
            raise Exception("A GameObject's matrix must be of type Matrix")
        self._matrix = value


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
