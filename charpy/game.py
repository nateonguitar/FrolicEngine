from abc import ABC, abstractmethod
import datetime
import threading
import time


from charpy.console_printer import ConsolePrinter
from charpy.input_controller import InputController
from charpy.screen import Screen

class Game(ABC):
    # convenient reference to the Game object
    instance = None

    def __init__(self, fps=60):
        self.target_fps = fps
        self.stopped = False
        self.show_debug_info = False
        self.debug_size = {
            'key': 0,
            'value': 0,
        }
        self.debug_info = {
            'FPS': 0,
            'Chars Replaced': 0,
        }
        self.screen = Screen()
        self.printer = None
        self.input_controller = None
        self.timer_thread = None
        self.printer = ConsolePrinter()
        self.input_controller = InputController(self)
        self.input_controller.start_watching_key_presses()
        self.printer.clear_screen()
        self.clear_set_empty_screen()
        Game.instance = self
        self.last_loop_start_time : datetime = datetime.datetime.now()


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
                val_width = len(str(value)) if value is not None else 0
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
        while True:
            loop_start_time = datetime.datetime.now()
            calc_time = loop_start_time - self.last_loop_start_time
            self.last_loop_start_time = loop_start_time

            if self.show_debug_info:
                self.calculate_debug(calc_time)

            self.update(calc_time)
            self.draw()

            if self.stopped:
                return

    #     # wait some time on a separate thread then run game_loop again
    #     # this avoids using a spin-lock

            # time.time
            frame_wait_timming = datetime.timedelta(microseconds=(1000 * 1000 / self.target_fps))


            loop_time_after_calc = datetime.datetime.now()
            calc_time = loop_time_after_calc - loop_start_time
            real_wait_time = frame_wait_timming - calc_time
            # print(f"will wait for: {real_wait_time.microseconds / 1000 / 1000}")
            time.sleep(real_wait_time.microseconds / 1000 / 1000)

    #     self.timer_thread = threading.Timer(next_frame_wait, self.game_loop)
    #     self.timer_thread.start()


    def calculate_debug(self, deltatime):
        if deltatime.microseconds == 0:
            self.debug_info['FPS'] = None
        else:
            self.debug_info['FPS'] = str(round(1000000 / deltatime.microseconds, 2))
        self.debug_info['Chars Replaced'] = ConsolePrinter.replaced


    def end_game(self):
        self.printer.clear_screen()
        self.stopped = True
        self.input_controller.stop_watching_key_presses()
        self.timer_thread.cancel()


    def set_on_keydown(self, func):
        self.input_controller.set_on_keydown(func)


    def set_on_keyup(self, func):
        self.input_controller.set_on_keyup(func)
