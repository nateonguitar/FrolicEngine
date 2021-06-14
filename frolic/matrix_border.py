class MatrixBorder():
    """
    ```
    MatrixBorder(sides=MatrixBorder.SINGLE_LINE_THIN)
    ```
    """
    SINGLE_LINE_THIN = {
        'top': '─',
        'top_left': '┌',
        'top_right': '┐',
        'left': '│',
        'right': '│',
        'bottom': '─',
        'bottom_left': '└',
        'bottom_right': '┘',
    }
    SINGLE_LINE_THICK = {
        'top': '━',
        'top_left': '┏',
        'top_right': '┓',
        'left': '┃',
        'right': '┃',
        'bottom': '━',
        'bottom_left': '┗',
        'bottom_right': '┛',
    }
    DOUBLE_LINE = {
        'top': '═',
        'top_left': '╔',
        'top_right': '╗',
        'left': '║',
        'right': '║',
        'bottom': '═',
        'bottom_left': '╚',
        'bottom_right': '╝',
    }
    STARS = {
        'top': '*',
        'top_left': '*',
        'top_right': '*',
        'left': '*',
        'right': '*',
        'bottom': '*',
        'bottom_left': '*',
        'bottom_right': '*',
    }


    def __init__(self, sides=SINGLE_LINE_THIN):
        self.top          = sides.get('top', None)
        self.top_left     = sides.get('top_left', None)
        self.top_right    = sides.get('top_right', None)
        self.left         = sides.get('left', None)
        self.right        = sides.get('right', None)
        self.bottom       = sides.get('bottom', None)
        self.bottom_left  = sides.get('bottom_left', None)
        self.bottom_right = sides.get('bottom_right', None)
        sides = (
            self.top,
            self.top_left,
            self.top_right,
            self.left,
            self.right,
            self.bottom,
            self.bottom_left,
            self.bottom_right,
        )
        for side in sides:
            if side == None:
                continue
            if type(side) is not str or len(side) != 1:
                raise Exception('Sides must be a single character each')
