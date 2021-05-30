import threading
from pynput import keyboard


class KeyPresses():
    def __init__(self):
        self.keep_from_dying_thread = None
        self.holding_shift = False
        self.key_listener = keyboard.Listener(on_press=self.on_keydown, on_release=self.on_keyup)
        self.key_listener.start()


    def on_keydown(self, key: keyboard.Key):
        char = hasattr(key, 'char')
        if char:
            if self.holding_shift and key.char.lower() == 'b':
                print('Shift B')
        else:
            if key == keyboard.Key.esc:
                self.key_listener.stop()
                self.keep_from_dying_thread.cancel()
            if key == keyboard.Key.shift:
                self.holding_shift = True


    def on_keyup(self, key: keyboard.Key):
        if key == keyboard.Key.shift:
            self.holding_shift = False


    def keep_from_dying(self):
        self.keep_from_dying_thread = threading.Timer(1000000, lambda : None)
        self.keep_from_dying_thread.start()


k = KeyPresses()
k.keep_from_dying()
