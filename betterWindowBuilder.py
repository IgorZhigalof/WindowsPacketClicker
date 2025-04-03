from betterWindow import BetterWindow
import ctypes


class BetterWindowBuilder:
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    title = ""
    clickTime = None
    pressTime = None
    writeDelayTime = None

    def setWindowTitle(self, title: str):
        self.title = title

    def findWindowsByTitle(self, title: str) -> int:
        return self.user32.FindWindowExW(None, None, None, title)

    def setClickDelay(self, time: int):
        self.clickTime = time

    def setPressTime(self, time):
        self.pressTime = time

    def setWriteDelayTime(self, time):
        self.pressTime = time

    def setDefaultDelay(self, time: int):
        self.clickTime = setIfNotNone(self.clickTime, time)
        self.pressTime = setIfNotNone(self.pressTime, time)
        self.writeDelayTime = setIfNotNone(self.writeDelayTime, time)

    def build(self):
        return BetterWindow(self.find_windows_by_title(self.title), self.time)


def setIfNotNone(param, value):
    if (param != None):
        return param
    else:
        return value