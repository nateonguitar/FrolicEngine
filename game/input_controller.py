from pynput import keyboard


class InputController():

    # handy reference
    game = None
    listener = None


    def __init__(self, game):
        self.game = game


    def start_watching_key_presses(self):
        self.listener = keyboard.Listener(
            on_press=self.on_keydown,
            on_release=self.on_keyup)
        self.listener.start()
    

    def stop_watching_key_presses(self):
        self.listener.stop()


    def on_keydown(self, key):
        print(key)
        if key == keyboard.Key.esc:
            self.game.end_game()


    def on_keyup(self, key):
        print(key)
