import math
import threading
import time

from pykeyboard import PyKeyboardEvent
from pymouse import PyMouseEvent

class MouseHook(PyMouseEvent):        

    def __init__(self, logdata):
        PyMouseEvent.__init__(self)
        self.logdata = logdata

        self.mouse_x = 0
        self.mouse_y = 0
        self.lastMoveTime = time.time()

    def click(self, x, y, button, press):
        # button = 1: 左键
        # button = 2: 右键
        # button = 3: 中键
        if press: 
            self.logdata.clickPosition.append([str(x) + ", " + str(y)])
            if button == 1:
                self.logdata.leftMouse += 1
            if button == 2:
                self.logdata.rightMouse += 1
            if button == 3:
                self.logdata.middleMouse += 1

    def calculateDistance(self, new_x, new_y):
        # 一个像素 0.3mm
        return math.sqrt((new_x - self.mouse_x) ** 2 + (new_y - self.mouse_y) ** 2) * 0.3 / 1000

    def move(self, x, y):
        cur_time = time.time()
        cur_dis = self.calculateDistance(x, y)

        self.logdata.mouseSpeed = max(cur_dis / (cur_time - self.lastMoveTime), self.logdata.mouseSpeed)
        self.logdata.mouseDistance += cur_dis
        # print("移动距离: " + str(self.logdata.mouseDistance))
        # print("当前移动速度: " + str(cur_dis / (cur_time - self.lastMoveTime)))
        # print("最大移动速度: " + str(self.logdata.keySpeed))

        self.mouse_x = x
        self.mouse_y = y
        self.lastMoveTime = cur_time

if __name__ == '__main__':
    # start()开启子线程, run()直接在主线程运行
    import sys
    sys.path.append('../')
    from keylistener.entity.LogData import LogData
    data = LogData()
    MouseHook(data).start()
    while True:
        time.sleep(1)
        print(data)
