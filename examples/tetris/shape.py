import numpy
from game.vector2 import Vector2


class Shape():

    matrix = []
    char = '▣'
    # Vector2
    position = None


    def spin(self):
        """
        transposing, then reversing rows gives O(n^2) time and O(1) space complexity
        """
        length = len(self.matrix)
        self.matrix = numpy.transpose(self.matrix)
        for row in range(0, length):
            start = 0
            end = length -1
            while (start < end) :
                self.matrix[row][start], self.matrix[row][end] = self.matrix[row][end], self.matrix[row][start]
                start += 1
                end -= 1
        return self.matrix

    @property
    def size(self):
        x = 0
        y = len(self.matrix)
        if y > 0:
            x = len(self.matrix[0])
        return Vector2(x=x, y=y)


    def __str__(self):
        return 'Shape'


class Square(Shape):
    matrix = [
        [1, 1],
        [1, 1],
    ]

    def __str__(self):
        return 'Square'

class Line(Shape):
    matrix = [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
    ]
    def __str__(self):
        return 'Line'


class ForwardsL(Shape):
    matrix = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
    ]
    def __str__(self):
        return 'ForwardsL'


class BackwardsL(Shape):
    matrix = [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 0],
    ]
    def __str__(self):
        return 'BackwardsL'


class ForwardsZ(Shape):
    matrix = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 1, 1],
    ]
    def __str__(self):
        return 'ForwardsZ'


class BackwardsZ(Shape):
    matrix = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 1, 0],
    ]
    def __str__(self):
        return 'BackwardsZ'


class TShape(Shape):
    matrix = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0],
    ]
    def __str__(self):
        return 'TShape'
