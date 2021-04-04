import os
import termcolor


class ConsolePrinter():


    def clear_screen(self):
        # shift everything up
        print('\033[2J')
        terminal_size = os.get_terminal_size()
        # print a space on every character of the terminal
        for line in range(0, terminal_size.lines):
            line_str = ''
            for column in range(0, terminal_size.columns):
                line_str += ' '
            print(line_str)


    # TODO: won't print at the right column, row works though
    def char_at(self, x, y, char, color='white'):
        _x = str(x)
        _y = str(y)
        print(f"\033[{_y};{_x}H")
        print(f"{termcolor.colored(char, color)}")
