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
