from window import Window
import time


class BetterWindow(Window):
    mouseDelay = 0
    writeDelay = 0
    pressDelay = 0

    def __init__(self, hwnd, write_delay=0, mouse_delay=0, press_delay=0):
        self.writeDelay = write_delay
        self.left_click_delay = mouse_delay
        self.pressDelay = press_delay
        super().__init__(hwnd)

    def holdKey(self, key, holdTime):
        """The time parameter represents 100 milliseconds per unit."""
        for i in range(holdTime):
            self.keyDown(key)
            time.sleep(0.1)
        self.keyUp(key)

    def holdLeftClick(self, holdTime, x, y):
        """The time parameter represents 100 milliseconds per unit."""
        for i in range(holdTime):
            self.leftClickAt(x, y)
            time.sleep(0.1)

    def fastPressKey(self, char: str):
        l_param = (self._scancodes[char.upper()] << 16) | 1
        self._user32.SendMessageA(self._hwnd,
                                  self._WM_KEYDOWN,
                                  self._scancodes[char.upper()],
                                  l_param
                                  )
        time.sleep(self.pressDelay)

    def writeText(self, text: str):
        for chr in text:
            self.sendChar(chr)
            time.sleep(self.writeDelay)

