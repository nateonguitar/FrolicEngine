from abc import ABC, abstractmethod
import datetime
import threading

from charpy.console_printer import ConsolePrinter
from charpy.input_controller import InputController
from charpy.screen import Screen

class Game(ABC):

    def __init__(self, fps=30):
        self.stopped = False
        self.debug_size = {
            'key': 0,
            'value': 0,
        }
        self.debug_info = {
            'fps': 0,
            'chars_replaced': 0,
        }
        self.screen = Screen()
        self.show_debug_info = False
        self.game_loop_speed = 1 / fps
        self.printer = None
        self.input_controller = None
        self.timer_thread = None
        self.printer = ConsolePrinter()
        self.input_controller = InputController(self)
        self.input_controller.start_watching_key_presses()
        self.printer.clear_screen()
        self.clear_set_empty_screen()
        self.current_time : datetime = datetime.datetime.now()


    def clear_set_empty_screen(self):
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

        if self.show_debug_info:
            for key in self.debug_info:
                value = self.debug_info[key]
                key_width = len(str(key))
                if key_width > self.debug_size['key']:
                    self.debug_size['key'] = key_width
                val_width = len(str(value))
                if val_width > self.debug_size['value']:
                    self.debug_size['value'] = val_width
            # + 2 for the colon + space we will use
            key_value_width = self.debug_size['key'] + self.debug_size['value'] + 2
            i = 0
            screen_width = self.printer.terminal_size.columns
            for key in self.debug_info:
                value = self.debug_info[key]
                _key = str(key).rjust(self.debug_size['key'])
                _value = str(value if value is not None else ' ').ljust(self.debug_size['value'])
                key_value = f'{_key}: {_value}'
                self.screen.set(screen_width - key_value_width, i, key_value)
                i += 1

        self.printer.draw_screen(self.screen)
        self.clear_set_empty_screen()


    def game_loop(self):
        new_time = datetime.datetime.now()
        deltatime = new_time - self.current_time
        self.current_time = new_time
        if self.show_debug_info:
            self.calculate_debug(deltatime)
        self.update(deltatime)
        self.draw()

        if self.stopped:
            return
        # wait some time on a separate thread then run game_loop again
        # this avoids using a spin-lock
        self.timer_thread = threading.Timer(self.game_loop_speed, self.game_loop)
        self.timer_thread.start()


    def calculate_debug(self, deltatime):
        if deltatime.microseconds == 0:
            self.debug_info['fps'] = None
        else:
            self.debug_info['fps'] = str(int(1000000 / deltatime.microseconds))
        self.debug_info['chars_replaced'] = ConsolePrinter.replaced


    def end_game(self):
        self.printer.clear_screen()
        self.stopped = True
        self.input_controller.stop_watching_key_presses()
        self.timer_thread.cancel()


    def set_on_keydown(self, func):
        self.input_controller.set_on_keydown(func)

    
    def set_on_keyup(self, func):
        self.input_controller.set_on_keyup(func)