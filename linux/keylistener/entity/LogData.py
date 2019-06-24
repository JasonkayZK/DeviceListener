#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import json
import uuid

import sys
sys.path.append('../')
from keylistener.app.Constant import Constant
from keylistener.jdbc.LogDataDaoImpl import LogDataDaoImpl

class LogData(object):

    def __init__(self):
        self.userId = None
        self.leftMouse = 0
        self.rightMouse = 0
        self.middleMouse = 0
        self.keyStroke = 0
        self.mouseDistance = 0
        self.ip = None
        self.mac = None

        # 需要清理Cache数据
        self.clickPosition = list()
        self.keyMap = dict()
        self.mouseSpeed = 0.0
        self.keySpeed = 0.0

        if not os.path.exists(Constant.DATALOG):
            self.makeCache()
            print("成功创建缓存文件")

        if Constant.SYNC:
            self.reloadCache()
            print("成功重载入数据")
    
        with open(Constant.DATALOG, mode='r', encoding='utf-8') as f:
            load_dict = json.load(f)
            # 无需刷新缓存数据
            self.userId = load_dict["user_id"]
            self.leftMouse = load_dict["left_mouse"]
            self.rightMouse = load_dict["right_mouse"]
            self.middleMouse = load_dict["middle_mouse"]
            self.keyStroke = load_dict["key_stroke"]
            self.mouseDistance = load_dict["mouse_distance"]
            self.ip = load_dict["ip"]
            self.mac = load_dict["mac"]

            # 需要清理Cache数据
            self.clickPosition = load_dict["click_position"]
            self.keyMap = load_dict["key_map"]
            self.mouseSpeed = load_dict["mouse_speed"]
            self.keySpeed = load_dict["key_speed"]

    def reloadCache(self):
        """
            Reload data to variables from database
        """
        self.leftMouse, self.rightMouse, self.middleMouse, self.mouseDistance, self.keyStroke = LogDataDaoImpl().findLast()
        self.updateCache()

    def updateCache(self):
        """
            update cache from local variables.
        """
        fileIn = None
        try:
            fileIn = open(Constant.DATALOG, mode='r', encoding='utf-8')
            data = json.load(fileIn)            
        except:
            print("Fail to load datalog!")
        finally:
            if fileIn is not None: 
                fileIn.close()

        data["left_mouse"] = self.leftMouse
        data["right_mouse"] = self.rightMouse
        data["middle_mouse"] = self.middleMouse
        data["mouse_distance"] = self.mouseDistance
        data["key_stroke"] = self.keyStroke
        data["mouse_speed"] = self.mouseSpeed
        data["click_positon"] = self.clickPosition
        data["key_speed"] = self.keySpeed
        data["key_map"] = self.keyMap

        fileOut = None
        try:
            fileOut = open(Constant.DATALOG, mode='w', encoding='utf-8')
            fileOut.write(json.dumps(data))
        except:
            print("Fail to reload datalog!")
        finally:
            if fileOut is not None:
                fileOut.close()

    def makeCache(self):
        """
            create datalog.json if not exist.
        """
        f = None
        try:
            f = open(Constant.DATALOG, mode='w', encoding='utf-8')
            data = {
                "user_id": Constant.USER,

                "left_mouse": 0,
                "right_mouse": 0,
                "middle_mouse": 0,
                "mouse_distance": 0,

                "mouse_speed": 0,
                "click_position": [],

                "key_stroke": 0,
                
                "key_speed": 0,
                "key_map": {},
                
                "ip": Constant.IP,
                "mac": Constant.MAC
            }
            f.write(json.dumps(data))
        except:
            print("Fail to makeCache file!")
        finally:
            if f is not None:
                f.close()

    def clearCache(self):
        self.clickPosition = list()
        self.keyMap = dict()
        self.mouseSpeed = 0
        self.keySpeed = 0

    def __repr__(self):
        return str(self.userId) + ", " + str(self.leftMouse) + ", " + str(self.rightMouse) + ", " + str(self.middleMouse) + ", " + str(self.keyStroke) + ", " + str(self.mouseDistance) + ", " + str(self.ip) + ", " + str(self.mac) + ", " + str(self.clickPosition) + ", " + str(self.keyMap) + ", " + str(self.mouseSpeed) + ", " + str(self.keySpeed)


if __name__ == '__main__':
    Constant.init()
    data = LogData()
    print(data)


