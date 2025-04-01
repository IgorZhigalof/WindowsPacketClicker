from window import Window
import time

class BetterWindow(Window):
    mouse_delay = 0
    write_delay = 0
    press_delay = 0

    def __init__(self, hwnd, write_delay=0, mouse_delay=0, press_delay=0):
        self.write_delay = write_delay
        self.left_click_delay = mouse_delay
        self.press_delay = press_delay
        super().__init__(hwnd)

    def holdKey(self, key, tme):
        """The time parameter represents 100 milliseconds per unit."""
        for i in range(tme):
            self.key_down(key)
            time.sleep(0.1)
        self.key_up(key)

    def holdLeftClick(self, tme, x, y):
        for i in range(tme):
            self.left_click_at(x, y)
            time.sleep(0.1)

    def fastPressKey(self, char: str):
        l_param = (self._scancodes[char.upper()] << 16) | 1
        self._user32.SendMessageA(self._hwnd,
                                  self._WM_KEYDOWN,
                                  self._scancodes[char.upper()],
                                  l_param
                                  )
        time.sleep(self.press_delay)

    def writeText(self, text: str):
        for chr in text:
            self.sendChar(chr)
            time.sleep(self.write_delay)

