import numpy
from game.vector2 import Vector2
from game.game_object import GameObject


class Shape(GameObject):

    char = '▣'

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


    def __str__(self):
        return 'Shape'


class Square(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [1, 1],
            [1, 1],
        ]

    def __str__(self):
        return 'Square'

class Line(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
        ]

    def __str__(self):
        return 'Line'


class ForwardsL(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
        ]

    def __str__(self):
        return 'ForwardsL'


class BackwardsL(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 0],
        ]

    def __str__(self):
        return 'BackwardsL'


class ForwardsZ(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 0, 0],
            [1, 1, 0],
            [0, 1, 1],
        ]

    def __str__(self):
        return 'ForwardsZ'


class BackwardsZ(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 1, 0],
        ]

    def __str__(self):
        return 'BackwardsZ'


class TShape(Shape):

    def __init__(self):
        super().__init__()
        self.matrix = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0],
        ]

    def __str__(self):
        return 'TShape'
