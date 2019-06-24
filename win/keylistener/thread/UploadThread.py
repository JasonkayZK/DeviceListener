#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import time
import urllib
import threading
import requests 
import os
import io
import csv

import sys
sys.path.append('../')
from keylistener.app.Constant import Constant
from keylistener.jdbc.LogDataDaoImpl import LogDataDaoImpl

class UploadThread(threading.Thread):

    def __init__(self,  logdata, threadID = "UploadThread_1", name="UploadThread"):
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.name = name
        self.logdata = logdata

    def uploadToMysql(self):
        LogDataDaoImpl().add(self.logdata)
        
    # TODO
    def uploadToHttp(self):
        pass
    
    def saveLocal(self):
        if not os.path.exists(Constant.FILENAME):
            f = None
            try:
                f = io.open(Constant.FILENAME, 'ab')
                f_csv = csv.writer(f)
                header = ['uid', 'insert_time', 'left_mouse', 'right_mouse', 'middle_mouse', 'mouse_speed', 'mouse_distance', 'click_position', 'key_stroke', 'key_speed', 'key_map']
                print([",".join('%s' % id for id in header)])
                f_csv.writerow([",".join('%s' % id for id in header)])
            except:
                print("Fail to create local save file!")
            finally:
                if f is not None:
                    f.close()

        try:
            f = io.open(Constant.FILENAME, 'ab')
            f_csv = csv.writer(f)
            data = [self.logdata.userId, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.logdata.leftMouse, self.logdata.rightMouse, self.logdata.middleMouse, self.logdata.mouseSpeed, self.logdata.mouseDistance, self.logdata.clickPosition, self.logdata.keyStroke, self.logdata.keySpeed, self.logdata.keyMap]
            f_csv.writerow([",".join('%s' % id for id in data)])
        # except:
        #     print("Fail to update local data")
        finally:
            if f is not None:
                f.close()


    def run(self):
        while True:
            time.sleep(Constant.SAVEINTERVAL * 60)
            print(self.logdata)
            try:
                if Constant.USEHTTP:
                    self.uploadToHttp()
                    print("Success to upload via HTTP!")
                if Constant.USEMYSQL:
                    self.uploadToMysql()
                    print("Success to insert into mysql!")
                if Constant.USELOCAL:
                    self.saveLocal()
                    print("Success to save local!")
            except Exception as e:
                print(e)
            finally:
                self.logdata.updateCache()
                print("Success to refresh Cache!")
                self.logdata.clearCache()
                print("Success to clear cache!")
                

if __name__ == '__main__':
    from keylistener.app.Constant import Constant
    Constant.init()
    from keylistener.entity.LogData import LogData
    UploadThread(LogData()).start()


# 线程安全测试

    # class ModifyThread(threading.Thread):

    #     def __init__(self,  logdata, lock, threadID = "ModifyThread_1", name="ModifyThread"):
    #         threading.Thread.__init__(self)

    #         self.lock = lock
    #         self.threadID = threadID
    #         self.name = name
    #         self.logdata = logdata

    #     def run(self):
    #         while True:
    #             try:
    #                 time.sleep(1)
    #                 data.keySpeed += 1
    #                 print("外部:" + str(data.keySpeed))

    #             except Exception as e:
    #                 print(e)


    # from keylistener.entity.LogData import LogData
    # Constant.init()
    # data = LogData()

    # lock = threading.Lock()

    # ModifyThread(data, lock).start()



