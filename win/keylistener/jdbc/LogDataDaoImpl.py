#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../')
from keylistener.jdbc.DBUtil import DBUtil

class LogDataDaoImpl(object):

    def add(self, logData):
        """
            Add data to db.
        """
        conn = None
        try:
            conn = DBUtil.getConnection()
            cursor = conn.cursor()

            sql = "INSERT INTO logger  \
                (uid, left_mouse, right_mouse, middle_mouse, mouse_speed, mouse_distance, click_position, key_stroke, key_speed, key_map, ip, mac) \
                VALUES \
                (\"%s\", %s, %s, %s, %s, %s, \"%s\", %s, %s, \"%s\", \"%s\", \"%s\");" % \
                (logData.userId, logData.leftMouse, logData.rightMouse, logData.middleMouse, logData.mouseSpeed, logData.mouseDistance, logData.clickPosition, logData.keyStroke, logData.keySpeed, logData.keyMap, logData.ip, logData.mac)

            if cursor.execute(sql) != 1:
                return Exception("Fail to insert data!")

            conn.commit()
            print("Success to insert!")
        # except:
        #     conn.rollback()
        #     print("Fail to add data into db!")
        finally:
            if conn is not None:
                DBUtil.close(conn)
        
    def delete(self, id):
        pass

    def find(self, id):
        pass

    def findLast(self):
        """
            Query last data in db, for loading cache.

            @return left_mouse, right_mouse, middle_mouse, mouse_distance, key_stroke
        """
        conn = None
        try:
            conn = DBUtil.getConnection()
            cursor = conn.cursor()

            sql = """select left_mouse, right_mouse, middle_mouse, mouse_distance, key_stroke from logger where id=(select max(id) from logger);"""

            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            if results is None or len(results) == 0:
                return 0, 0, 0, 0.0, 0
            else:
                for row in results:
                    return row[0], row[1], row[2], row[3], row[4]

        except:
            print ("Error: unable to fetch data")
        finally:
            if conn is not None:
                DBUtil.close(conn)

    # TODO
    def findAll(self):
        pass

    # TODO
    def modify(self, id):
        pass

if __name__ == '__main__':
    from keylistener.app.Constant import Constant
    Constant.init()
    logDataDaoImpl = LogDataDaoImpl()
    print(logDataDaoImpl.findLast())

    from keylistener.entity.LogData import LogData
    data = LogData()
    logDataDaoImpl.add(data)
    