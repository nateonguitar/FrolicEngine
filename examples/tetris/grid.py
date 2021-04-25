from game import Vector2

class Grid():
    # The matrix will look something like this, but its size
    # is set by the gridsize handed in to the constructor
    # ╔═══╗
    # ║°°°║
    # ║°°°║
    # ║°°°║
    # ╚═══╝

    size = Vector2(x=13, y=16)
    position = Vector2(x=5, y=0)
    matrix = []
    empty_char = '.' # '°'

    def __init__(self):

        # fill the matrix with the emtpy char
        for i in range(0, self.size.y):
            row = []
            for j in range(0, self.size.x):
                row.append(self.empty_char)
            self.matrix.append(row)
        
        # swap the edges for box characters
        # swap the corners
        self.matrix[0][0] = '╔'
        self.matrix[0][self.size.x-1] = '╗'
        self.matrix[self.size.y-1][0] = '╚'
        self.matrix[self.size.y-1][self.size.x-1] = '╝'

        # swap top and bottoms with '═' (skipping first and last positions)
        for i in range(1, self.size.x-1):
            self.matrix[0][i] = '═'
            self.matrix[self.size.y-1][i] = '═'

        # swap left and right sides with '║' (skipping first and last positions)
        for row in self.matrix:
            # we have already swapped the corners, so we can rely on checking that
            if row[0] == self.empty_char:
                row[0] = '║'
                row[self.size.x-1] = '║'
