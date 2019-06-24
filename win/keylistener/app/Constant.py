#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import uuid
import io
import socket

class Constant(object):

    SAVEINTERVAL = 5,
    USEMYSQL = False
    USEHTTP = False
    USELOCAL = False
    FILENAME = 'logger.csv'
    DATALOG = 'datalog.json'
    SYNC = False

    MAC = 'NO MAC'
    IP = '127.0.0.1'
    USER = 'localhost'

    DB_HOST = ""
    DB_PORT = 3306
    DB_DBNAME = ""
    DB_USERNAME = ""
    DB_PASSWORD = ""

    @staticmethod
    def init():
        with io.open('config.json', mode='r', encoding='utf-8') as f:
            load_dict = json.load(f)
            Constant.SAVEINTERVAL = load_dict["save"]["saveInterval"]
            Constant.USEHTTP = load_dict["save"]["useHttp"]
            Constant.USEMYSQL = load_dict["save"]["useMysql"]
            Constant.USELOCAL = load_dict["save"]["useLocal"]
            Constant.FILENAME = load_dict["save"]["filename"]
            Constant.DATALOG = load_dict["datalog"]
            Constant.SYNC = load_dict["sync"]

            Constant.DB_HOST = load_dict["database"]["host"]
            Constant.DB_PORT = load_dict["database"]["port"]
            Constant.DB_DBNAME = load_dict["database"]["dbname"]
            Constant.DB_USERNAME = load_dict["database"]["username"]
            Constant.DB_PASSWORD = load_dict["database"]["password"]

            Constant.MAC = Constant.getMacAddress()
            Constant.IP = Constant.getIp()
            Constant.USER = Constant.getUsername()


    @staticmethod
    def getMacAddress():
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
        return ":".join([mac[e:e+2] for e in range(0,11,2)])

    @staticmethod
    def getUsername():
        return socket.gethostname()

    @staticmethod
    def getIp():
        return socket.gethostbyname(socket.gethostname())



if __name__ == '__main__':
    Constant.init()
    print(Constant.DATALOG)
    if not Constant.USEHTTP:
        print('ok')


