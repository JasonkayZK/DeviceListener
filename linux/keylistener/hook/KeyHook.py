from pykeyboard import PyKeyboardEvent
import time

class KeyHook(PyKeyboardEvent):
    def __init__(self, logdata):
        PyKeyboardEvent.__init__(self)
        self.logdata = logdata

        self.lastTime = time.time()
        self.lastStrokeVolume = self.logdata.keyStroke

    def tap(self, keycode, character, press):
        if press:
            self.logdata.keyStroke += 1
            if character in self.logdata.keyMap:
                self.logdata.keyMap[character] += 1
            else:
                self.logdata.keyMap[character] = 1

            if time.time() - self.lastTime >= 3:
                self.logdata.keySpeed = max(self.logdata.keySpeed, (self.logdata.keyStroke - self.lastStrokeVolume) / (time.time() - self.lastTime))
                self.lastTime = time.time()

if __name__ == '__main__':
    # start()开启子线程, run()直接在主线程运行
    import sys
    sys.path.append('../')
    from keylistener.entity.LogData import LogData
    data = LogData()
    KeyHook(data).start()
    while True:
        pass
        time.sleep(1)
        print(data)    

