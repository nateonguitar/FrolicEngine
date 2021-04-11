import os


class ConsolePrinter():
    
    ansi_start = "\033["
    ansi_end = "\033[0m"
    previous_screen = []


    def __init__(self):
        self.previous_screen = self.get_empty_screen()


    def get_empty_screen(self):
        terminal_size = os.get_terminal_size()
        screen = []
        for line_number in range(0, terminal_size.lines):
            line = []
            for column_number in range(0, terminal_size.columns):
                line.append(' ')
            screen.append(line)
        return screen


    def clear_screen(self):
        terminal_size = os.get_terminal_size()
        # print a space on every character of the terminal
        for line in range(0, terminal_size.lines):
            line_str = ''
            for column in range(0, terminal_size.columns):
                line_str += ' '
            print(f"{self.ansi_start}{column+1};0H{line_str}{self.ansi_end}")


    # TODO: colors not working yet
    def char_at(self, x, y, char, color='white'):
        position = f"{y+1};{x}H"
        print(f"{self.ansi_start}{position}{char}{self.ansi_end}")

    
    def draw_screen(self, screen):
        # Print over the entire screen with what has been stored
        # in our screen representation.
        # Only prints over characters that have changed since the last print.
        lines = len(screen)
        columns = len(screen[0])
        for line in range(0, lines):
            for column in range(0, columns):
                prev_char = self.previous_screen[line][column]
                new_char = screen[line][column]
                if new_char != prev_char:
                    self.char_at(column, line, new_char)

        # So we don't leave the cursor in an annoying place between draws
        # we will draw the final character at the bottom right corner
        bottom_right_char = screen[lines-1][columns-1]
        self.char_at(columns-1, lines-2, bottom_right_char)

        # Store the current state of the screen so we can
        # use it again next cycle
        self.previous_screen = screen
