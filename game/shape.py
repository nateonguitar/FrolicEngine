class Shape():
    shape_array_up, shape_array_down, shape_array_right, shape_array_left = [], [], [], []
    orientation = 'u'

    def __init__(self):
        self.orientation = 'u'

    def get_shape(self):
        if self.orientation == 'u':
            return self.shape_array_up

        if self.orientation == 'r':
            return self.shape_array_right

        if self.orientation == 'd': 
            return self.shape_array_down

        if self.orientation == 'l':
            return self.shape_array_left

    def spin(self):
        if self.orientation == 'u':
            self.orientation = 'r'
            return self.shape_array_right

        if self.orientation == 'r':
            self.orientation = 'd'
            return self.shape_array_down

        if self.orientation == 'd': 
            self.orientation = 'l'
            return self.shape_array_left

        if self.orientation == 'l':
            self.orientation = 'u'
            return self.shape_array_up
    
class Square(Shape):
    shape_array_up = [
        ['▣','▣'],
        ['▣','▣']
    ]

    shape_array_down = [
        ['▣','▣'],
        ['▣','▣']
    ]

    shape_array_left = [
        ['▣','▣'],
        ['▣','▣']
    ]

    shape_array_right = [
        ['▣','▣'],
        ['▣','▣']
    ]

class Line(Shape):
    shape_array_up = [
        ['▣'],
        ['▣'],
        ['▣'],
        ['▣']
    ]
    
    shape_array_down = [
        ['▣'],
        ['▣'],
        ['▣'],
        ['▣']
    ]

    shape_array_left = [
        ['▣', '▣', '▣', '▣']
    ]
    
    shape_array_right = [
        ['▣', '▣', '▣', '▣']
    ]
    
class ForwardsL(Shape):
    shape_array_up = [
        ['▣'],
        ['▣'],
        ['▣','▣']
    ]

    shape_array_down = [
        ['▣', '▣'],
        [' ', '▣'],
        [' ', '▣'],
    ]

    shape_array_left = [
        [' ', ' ', '▣'],
        ['▣', '▣', '▣']
    ]

    shape_array_right = [
        ['▣', '▣', '▣'],
        ['▣', ' ', ' ']
    ]

class BackwardsL(Shape):
    shape_array_up = [
        [' ', '▣'],
        [' ', '▣'],
        ['▣', '▣']
    ]

    shape_array_down = [
        ['▣', '▣'],
        ['▣', ' '],
        ['▣', ' '],
    ]

    shape_array_left = [
        ['▣', ' ', ' '],
        ['▣', '▣', '▣']
    ]

    shape_array_right = [
        ['▣', '▣', '▣'],
        [' ', ' ', '▣']
    ]

class ForwardsZ(Shape):
    shape_array_up = [
        ['▣', '▣'],
        [' ', '▣', '▣'],
    ]

    shape_array_down = [
        ['▣', '▣', ' '],
        [' ', '▣', '▣'],
    ]

    shape_array_left = [
        [' ', '▣'],
        ['▣', '▣'],
        ['▣', ' ']
    ]

    shape_array_right = [
        [' ', '▣'],
        ['▣', '▣'],
        ['▣', ' ']
    ]

class BackwardsZ(Shape):
    shape_array_up = [
        [' ', '▣', '▣'],
        ['▣', '▣', ' '],
    ]

    shape_array_down = [
        [' ', '▣', '▣'],
        ['▣', '▣', ' '],
    ]

    shape_array_left = [
        ['▣', ' '],
        ['▣', '▣'],
        [' ', '▣']
    ]

    shape_array_right = [
        ['▣', ' '],
        ['▣', '▣'],
        [' ', '▣']
    ]

class TShape(Shape):
    shape_array_up = [
        [' ', '▣', ' '],
        ['▣', '▣', '▣'],
    ]

    shape_array_down = [
        ['▣', '▣', '▣'],
        [' ', '▣', ' '],
    ]

    shape_array_left = [
        [' ', '▣'],
        ['▣', '▣'],
        [' ', '▣']
    ]

    shape_array_right = [
        ['▣', ' '],
        ['▣', '▣'],
        ['▣', ' ']
    ]