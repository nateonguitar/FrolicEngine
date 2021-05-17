from game import Game
from examples.tetris import TetrisGame


class AvailableGame():
    def __init__(self, label: str, game_class: Game, description: str = ''):
        self.label: str = label
        self.description: str = description
        self.game_class: Game = game_class



available_games = (
    AvailableGame(label='Tetris', game_class=TetrisGame, description="It's Tetris baby!"),
)
print('')
for i in range(0, len(available_games)):
    g = available_games[i]
    print(f'{i}: {g.label} | {g.description}')
print('')

GameChoice = None
try:
    choice = input('Choose a game by number: ')
    choice_int = int(choice)
    if choice_int < 0:
        raise Exception('Input not in range')
    GameChoice = available_games[choice_int].game_class
except:
    print('\nbad input\n')

if GameChoice:
    game = GameChoice()
