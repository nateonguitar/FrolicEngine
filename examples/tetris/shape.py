import numpy


class Shape():

    matrix = []
    char = '▣'
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


class Square(Shape):
    matrix = [
        [1, 1],
        [1, 1],
    ]


class Line(Shape):
    matrix = [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
    ]


class ForwardsL(Shape):
    matrix = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
    ]


class BackwardsL(Shape):
    matrix = [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 0],
    ]


class ForwardsZ(Shape):
    matrix = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 1, 1],
    ]


class BackwardsZ(Shape):
    matrix = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 1, 0],
    ]


class TShape(Shape):
    matrix = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0],
    ]
