from abc import ABC, abstractmethod
import os
import threading
import datetime

from .input_controller import InputController
from .console_printer import ConsolePrinter

class Game(ABC):

    def __init__(self, fps=30):
        self.stopped = False
        self.screen = []
        self.game_loop_speed = 1 / fps
        self.printer = None
        self.input_controller = None
        self.timer_thread = None
        self.printer = ConsolePrinter()
        self.input_controller = InputController(self)
        self.input_controller.start_watching_key_presses()
        self.printer.clear_screen()
        self.empty_screen()
        self.current_time : datetime = datetime.datetime.now()


    def empty_screen(self):
        self.screen = self.printer.get_empty_screen()


    @abstractmethod
    def update(self, deltatime:datetime.timedelta):
        pass


    @abstractmethod
    def draw(self):
        # The Strategy:
        # Every draw cycle will print to every position in the console.
        # We need to build a 2D array of what should be printed.
        # So we create a "screen" 2D array that is filled with spaces,
        # then replace values at certain positions.
        # Then we only do a print cycle once everything is in place.
        self.printer.draw_screen(self.screen)
        self.empty_screen()


    def game_loop(self):
        new_time = datetime.datetime.now()
        deltatime = new_time - self.current_time
        self.current_time = new_time
        self.update(deltatime)
        self.draw()

        if self.stopped:
            return
        # wait some time on a separate thread then run game_loop again
        # this avoids using a spin-lock
        self.timer_thread = threading.Timer(self.game_loop_speed, self.game_loop)
        self.timer_thread.start()


    def end_game(self):
        self.stopped = True
        self.input_controller.stop_watching_key_presses()
        self.timer_thread.cancel()
        self.printer.clear_screen()


    def set_on_keydown(self, func):
        self.input_controller.set_on_keydown(func)

    
    def set_on_keyup(self, func):
        self.input_controller.set_on_keyup(func)