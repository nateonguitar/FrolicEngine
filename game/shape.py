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
    shape_array = [
        ['▣','▣'],
        ['▣','▣']
    ]

    def spin(self):
        return self.shape_array

    def get_shape(self):
        return self.shape_array
              

class Line(Shape):
    shape_array = [
        ['▣'],
        ['▣'],
        ['▣'],
        ['▣']
    ]
    
    shape_array_side = [
        ['▣', '▣', '▣', '▣']
    ]
        
    def get_shape(self):
        if self.orientation == 'u':
            return self.shape_array

        if self.orientation == 'r':
            return self.shape_array_side

        if self.orientation == 'd': 
            return self.shape_array

        if self.orientation == 'l':
            return self.shape_array_side
      
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
