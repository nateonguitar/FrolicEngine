import os


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


    # TODO: colors not working yet
    def char_at(self, x, y, char, color='white'):
        _x = str(x)
        _y = str(y)
        ansi_start = "\033["
        ansi_end = "\033[0m"
        position = f"{y+1};{_x}H"
        print(f"{ansi_start}{position}{char}{ansi_end}")
