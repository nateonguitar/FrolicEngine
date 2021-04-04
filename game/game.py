import os
import threading
from .input_controller import InputController
from .console_printer import ConsolePrinter


class Game():
    game_over = False
    current_speed = 0.5
    time_between_draws = 0.5
    printer = None
    input_controller = None
    timer_thread = None


    def start(self):
        self.printer = ConsolePrinter()
        self.input_controller = InputController(self)
        self.input_controller.start_watching_key_presses()
        self.game_loop()


    def update(self):
        print('update')


    def draw(self):
        self.printer.clear_screen()
        self.printer.char_at(5, 5, 'W')
        print('draw')


    def game_loop(self):
        self.update()
        self.draw()

        if self.game_over:
            # stop the game loop
            return

        # wait some time on a separate thread then run game_loop again
        # this avoids using a spin-lock
        self.timer_thread = threading.Timer(self.time_between_draws, self.game_loop)
        self.timer_thread.start()


    def end_game(self):
        self.input_controller.stop_watching_key_presses()
        self.timer_thread.cancel()
