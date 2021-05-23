import datetime
from charpy import Game, GameObject, Matrix, MatrixBorder, Vector2

class Card(GameObject):
    def __init__(self):
        super().__init__()
        self.position = Vector2(x=2, y=2)
        self.matrix = Matrix.empty_sized(rows=6, columns=6, value=' ')
        self.matrix[1][1] = '2'
        # ♤ ♡ ♧ ♢
        self.matrix[2][1] = '♤'


class TestGame(Game):
    def __init__(self):
        super().__init__()
        self.card = Card()
        self.time_between_border_swaps = 1 # seconds
        self.time_since_swap = 0
        self.borders = (
            MatrixBorder(MatrixBorder.SINGLE_LINE_THIN),
            MatrixBorder(MatrixBorder.SINGLE_LINE_THICK),
            MatrixBorder(MatrixBorder.DOUBLE_LINE),
            MatrixBorder({
                'top': '*',
                'top_left': '*',
                'top_right': '*',
                'left': '*',
                'right': '*',
                'bottom': '*',
                'bottom_left': '*',
                'bottom_right': '*',
            })
        )
        self.current_border_index = 0

    def update(self, deltatime: datetime.timedelta):
        self.time_since_swap += deltatime.total_seconds()
        if self.time_since_swap >= self.time_between_border_swaps:
            self.time_since_swap = 0
            self.current_border_index += 1
            if self.current_border_index >= len(self.borders):
                self.current_border_index = 0

    def draw(self):
        self.screen.set(0, 0, 'press w to swap borders')
        _border = self.borders[self.current_border_index]
        _matrix = self.card.matrix.with_border(_border)
        self.screen.draw_matrix(_matrix, self.card.position)
        super().draw()

game = TestGame()
game.game_loop()
