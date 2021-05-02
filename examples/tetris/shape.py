import numpy
from game.vector2 import Vector2
from game.game_object import GameObject
from game.matrix import Matrix


class Shape(GameObject):
    char = '▣'

    def __str__(self):
        return 'Shape'


class Square(Shape):
    def __init__(self):
        matrix = Matrix([
            [1, 1],
            [1, 1],
        ])
        super().__init__(matrix=matrix)

    def __str__(self):
        return 'Square'

class Line(Shape):
    char = '▤'
    def __init__(self):
        matrix = Matrix([
            [1],
            [1],
            [1],
            [1],
        ])
        super().__init__(matrix=matrix)

    def __str__(self):
        return 'Line'


class ForwardsL(Shape):
    char = '▢'
    def __init__(self):
        matrix = Matrix([
            [1, 0],
            [1, 0],
            [1, 1],
        ])
        super().__init__(matrix=matrix)

    def __str__(self):
        return 'ForwardsL'


class BackwardsL(Shape):
    char = '□'
    def __init__(self):
        matrix = Matrix([
            [0, 1],
            [0, 1],
            [1, 1],
        ])
        super().__init__(matrix=matrix)

    def __str__(self):
        return 'BackwardsL'


class ForwardsZ(Shape):
    char = '▧'
    def __init__(self):
        matrix = Matrix([
            [1, 1, 0],
            [0, 1, 1],
        ])
        super().__init__(matrix=matrix)

    def __str__(self):
        return 'ForwardsZ'


class BackwardsZ(Shape):
    char = '▨'
    def __init__(self):
        matrix = Matrix([
            [0, 1, 1],
            [1, 1, 0],
        ])
        super().__init__(matrix=matrix)

    def __str__(self):
        return 'BackwardsZ'


class TShape(Shape):
    char = '▦'
    def __init__(self):
        matrix = Matrix([
            [0, 1, 0],
            [1, 1, 1],
        ])
        super().__init__(matrix=matrix)

    def __str__(self):
        return 'TShape'
