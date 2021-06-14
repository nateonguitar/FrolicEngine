from frolic.game import Game
from frolic.matrix import Matrix
from frolic.vector2 import Vector2

class GameObject():

    def __init__(self, **kwargs):
        # for type hinting
        self._matrix: Matrix = None
        self._position: Vector2 = None
        # set the real thing
        self.matrix = kwargs.get('matrix', Matrix())
        self.position = kwargs.get('position', Vector2(x=0, y=0))
        

    @property
    def game_instance(self):
        return Game.instance


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
        """
        Computes and returns a Vector2 that holds the current size of self.matrix
        """
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
