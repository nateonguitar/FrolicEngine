from pynput import keyboard


class InputController():

    # handy reference
    listener = None
    on_keydown_callback = None
    on_keyup_callback = None

    def __init__(self, game):
        self.game = game


    def set_on_keydown(self, func):
        self.on_keydown_callback = func


    def set_on_keyup(self, func):
        self.on_keyup_callback = func


    def start_watching_key_presses(self):
        self.listener = keyboard.Listener(
            on_press=self.on_keydown,
            on_release=self.on_keyup)
        self.listener.daemon = True
        self.listener.start()
    

    def stop_watching_key_presses(self):
        self.listener.stop()


    def on_keydown(self, key):
        if self.on_keydown_callback:
            self.on_keydown_callback(key)

    def on_keyup(self, key):
        if self.on_keyup_callback:
            self.on_keyup_callback(key)
