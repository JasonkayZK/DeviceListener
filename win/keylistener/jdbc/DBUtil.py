#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql

import sys
sys.path.append('../')
from keylistener.app.Constant import Constant

class DBUtil(object):

    @staticmethod
    def getConnection():
        return pymysql.connect(host=Constant.DB_HOST, port=Constant.DB_PORT, user=Constant.DB_USERNAME, password=Constant.DB_PASSWORD, database=Constant.DB_DBNAME, charset='utf8')

    @staticmethod
    def close(conn):
        conn.close()

if __name__ == '__main__':
    Constant.init()
    conn = DBUtil.getConnection()
    DBUtil.close(conn)