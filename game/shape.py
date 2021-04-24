import numpy

class Shape():
    shape_array = []
    shape_char = '▣'


    def __init__(self):
        self.shape_char = '▣'

    # when using in Game, if shape_array[0][0](or w/e) == False, use background 
    def get_shape(self):
        return self.shape_array

    def get_shape_char(self):
        return self.shape_char

    # transposing, then reversing rows gives O(n^2) time and O(1) space complexity
    def spin(self):
        length = len(self.shape_array)
        

        self.shape_array = numpy.transpose(self.shape_array)

        for row in range(0, length):    
            start = 0
            end = length -1      
            while (start < end) :
                self.shape_array[row][start], self.shape_array[row][end] = self.shape_array[row][end], self.shape_array[row][start]
                start += 1
                end -= 1

        return self.shape_array
    
class Square(Shape):
    shape_array = [
        [True,True],
        [True,True]
    ]

class Line(Shape):
    shape_array = [
        [False, True, False, False],
        [False, True, False, False],
        [False, True, False, False],
        [False, True, False, False]
    ]
    
    
class ForwardsL(Shape):
    shape_array = [
        [True, False, False],
        [True, False, False],
        [True,True, False]
    ]

class BackwardsL(Shape):
    shape_array = [
        [False, True, False],
        [False, True, False],
        [True, True, False]
    ]

class ForwardsZ(Shape):
    shape_array = [
        [False, False, False],
        [True, True, False],
        [False, True, True],
    ]


class BackwardsZ(Shape):
    shape_array = [
        [False, False, False],
        [False, True, True],
        [True, True, False],
    ]

class TShape(Shape):
    shape_array = [
        [False, True, False],
        [True, True, True],
        [False, False, False]
    ]
